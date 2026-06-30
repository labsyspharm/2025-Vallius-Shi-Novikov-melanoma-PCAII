import cv2
import numpy as np


def labeled_mask_to_polygon(labeled_mask, mode="in"):
    assert mode in ["in", "on"]
    exteriors, _ = cv2.findContours(
        labeled_mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE
    )
    # when given an "int32" labeled mask, the `findContours` will return ~2
    # exteriors per label, the exterior coordinates will be -
    # 1. "on" the pixels of that label, the pixel value of the indicies is that
    #    label
    # 2. "on the outside" of the pixels of that label, the pixel value is 0
    cols, rows = np.array([cc[0] for cc in exteriors]).T
    pixel_values = labeled_mask[rows, cols].squeeze()
    # only keeps exteriors 1 (see above comment)
    is_on_labels = pixel_values > 0
    labels = pixel_values[is_on_labels]
    del pixel_values, cols, rows

    contours = np.empty_like(labels, dtype="object")
    idx = 0
    for coords, is_on in zip(exteriors, is_on_labels):
        if not is_on:
            continue
        # cannot form polygon with less than 3 points
        if len(coords) < 3:
            contours[idx] = None
            idx += 1
            continue
        polygon = np.vstack([coords.squeeze(), coords.squeeze()[0]])
        if mode == "on":
            import shapely

            polygon = (
                np.array(
                    shapely.Polygon(polygon)
                    .buffer(0.5, join_style="mitre")
                    .exterior.coords
                )
                .round(2)
                .astype("float32")
            )
        contours[idx] = polygon
        idx += 1

    sorting = np.argsort(labels)
    return {"label": labels[sorting], "contour": contours[sorting]}


import gzip
import json
import pathlib
import uuid

import pandas as pd
import tifffile
import tqdm
import matplotlib.colors
import skimage.exposure


df_feature = pd.read_csv(r"C:\Users\yc296\Downloads\MEL14_RCNG_data.csv")
customColors = {
    "RCNG1": "#D52928",
    "RCNG2": "#8E0000",
    "RCNG3": "#BC714A",
    "RCNG4": "#A7A9AC",
    "RCNG5": "#2B3990",
    "RCNG6": "#FFF800",
    "RCNG7": "#8DC63F",
    "RCNG8": "#8D00C1",
    "RCNG9": "#F7941D",
    "RCNG10": "#FF00ED",
    "RCNG11": "#27AAE1",
}
colors = {
    kk: skimage.exposure.rescale_intensity(
        np.asarray(matplotlib.colors.hex2color(vv)), in_range=(0, 1), out_range="uint8"
    )
    .round()
    .astype("uint8")
    for kk, vv in customColors.items()
}
df_feature["color"] = df_feature["spatial_cluster_RCNG"].map(colors)
df_feature = (
    df_feature[["CellID", "spatial_cluster_RCNG", "color"]].set_index("CellID").T
)


cell_mask_path = r"\\research.files.med.harvard.edu\HITS\lsp-analysis\cycif-production\16-Pre-Cancer-Atlas-for-Melanoma\PCAII_p16_e24\mcmicro_done\13Cycles\LSP11315\segmentation\unmicst-LSP11315\cell-zlib.ome.tif"


def mcmicro_mask_to_qupath(cell_mask_path, nucleus_mask_path=None):
    cell_mask_path = pathlib.Path(cell_mask_path)
    cell_contours = labeled_mask_to_polygon(tifffile.imread(cell_mask_path))

    df = pd.DataFrame(cell_contours).set_index("label")
    df.rename(columns={"contour": "contour-cell"}, inplace=True)

    df["contour-nucleus"] = 0
    if nucleus_mask_path is not None:
        nucl_contours = labeled_mask_to_polygon(tifffile.imread(nucleus_mask_path))
        df["contour-nucleus"] = pd.DataFrame(nucl_contours).set_index("label")

    df.dropna(inplace=True)
    df["uuid"] = df.index.map(lambda _: str(uuid.uuid4()))

    out_path = cell_mask_path.parent / f"{cell_mask_path.name.split('.')[0]}.geojson.gz"
    last = df.index[-1]
    with gzip.open(out_path, "wt", encoding="utf-8") as f:
        f.write("[\n")
        for idx, uid, c_nuc, c_cell in tqdm.tqdm(
            df[["uuid", "contour-nucleus", "contour-cell"]].itertuples(index=True),
            total=len(df),
        ):
            nucl_geom = {}
            if nucleus_mask_path is not None:
                nucl_geom = {
                    "nucleusGeometry": {
                        "type": "Polygon",
                        "coordinates": [c_nuc.tolist()],
                    }
                }
            nn, cc = df_feature.get(
                idx, default=("Ignore", np.full(3, 25, dtype="uint8"))
            )
            row_dict = {
                "type": "Feature",
                "id": uid,
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [c_cell.tolist()],
                },
                **nucl_geom,
                "properties": {
                    "objectType": "cell",
                    "measurements": {"label": idx},
                    "classification": {"name": nn, "color": cc.tolist()},
                },
            }
            line_break = "\n" if idx == last else ",\n"
            f.write(json.dumps(row_dict) + line_break)
        f.write("]")
