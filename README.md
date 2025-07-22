# **Quantifying the influence of spatial variation in the microenvironment on intra-tumoral heterogeneity in primary cutaneous melanoma**
------------------ 
TABLE OF CONTENTS
------------------
​
* GENERAL INFORMATION
  * ASSOCIATED PUBLICATION
  * RECOMMENDED CITATION
  * USEFUL LINKS
* ACCESS THE DATASET
  * FILE ORGANIZATION
  * REPOSITORY LINKS
  * FILE LIST
* ADDITIONAL NOTES/COMMENTS
​
--------------------
GENERAL INFORMATION
--------------------
​
**Quantifying the influence of spatial variation in the microenvironment on intra-tumoral heterogeneity in primary cutaneous melanoma** <Publication or Dataset Title>   
-
**Authors:** Tuulia Vallius#, Yingxiao Shi#, Edward Novikov#, Shishir M Pant, Roxanne Pelletier, Yu-An Chen, Juliann B. Tefft, Ajit Nirmal Johnson, Zoltan Maliga, Guihong Wan, George Murphy, Sandro Santagata, Yevgeniy R Semenov, David Liu, Christine G Lian+, and Peter K Sorger+.  
  
#Co-first Authors: T.V., Y.S., E.N.  
+Co-Senior Authors: C.G.L., P.K.S.  
​  
**Please cite this data as the following:**      
Vallius, T. et al. (2025). Quantifying the influence of spatial variation in the microenvironment on intra-tumoral heterogeneity in primary cutaneous melanoma. {journal/biorxv}    

**Relevant links:** <remove links that are not relevant>  
> * Publication DOI: [doi.org/MY-PAPER-DOI](https://doi.org/MY-PAPER-DOI-URL) 
> * Associated GitHub Repository: [MY-REPO](https://github.com/labsyspharm/2025-Vallius-Shi-Novikov-melanoma-PCAII)  
> * To view an archived record of this repository: [My-ZENODO-DOI](https://zenodo.org/doi/MY-ZENODO-DOI-URL) 
> * To view the image data online, visit: [My-ATLAS-PAGE](https://tissue-atlas.org/MY-ATLAS-PAGE-URL)
​
**Licenses/restrictions placed on the data:** CC-BY [creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
​
--------------------
ACCESS THE DATASET 
--------------------

## File organization:   
**Each file follows the following naming convention:**    
​
Each file corresponds to a patient sample (N).
 
|File Type                                     | Description                                                                        | Location  |
|--------                                      | -----------------------------------------------------------------------------------|-----------|
|N.ome.tif                                     | Stitched multiplex CyCIF image pyramid in ome.tif format                           | HTAN, AWS |
|N.ome.tif                                     | Hematoxylin and Eosin stained image of adjacent FFPE tissue section                | HTAN, AWS |
|N-mask-cell.ome.tif                           | Segmentation mask image                                                            | HTAN, AWS |
|unmicst-N_cell.csv OR N--unmicst_cellRing.csv | Single-cell feature table, including intensity data for all channels               | HTAN, AWS |
|N.fastq                                       | Sequencing data                                                                    | GEO       |


## AWS Data Access  
Full-resolution CyCIF images, single cell segmentation masks, and cell count tables will be available via AWS.
​
**You will need the following bucket name:**  
```
AWS BUCKET NAME  
```
​
*For general instructions on how to download data from AWS, see: [https://zenodo.org/records/10223574](https://zenodo.org/records/10223574)*     
  
If you experience issues accessing the above AWS S3 buckets, email tissue-atlas(at)hms.harvard.edu with the subject line "bucketname: Data Access".  

## GEO Data Access
GeoMx gene expression data will be available via the Gene Expression Omnibus (GEO). 
​
## Other Data Access 
All images will be available to explore online (via Minerva, no download required) at the Harvard Tissue Atlas (https://www.tissue-atlas.org/).  Selected CyCIF channels for specimen MEL14 can be explored via Minerva at {add link}.

Full-resolution CyCIF images, single cell segmentation masks, and cell count tables will be available via the NCI Human Tumor Atlas Network data portal (https://data.humantumoratlas.org/)​





​
## FILE LIST  
### CyCIF Image Data
|Patient ID | File Name        | Location | File size | CyCIF Panel |
|------------------------- | -----------------|----------|-----------| ----------- |
MEL14	| LSP11314.ome.tif	| HTAN, AWS	| 420.049 GB |	p16_e41_PCAII_tumorintrinsic
MEL14	| LSP11315.ome.tif |	HTAN, AWS |	359.303 GB	| RP-p16-e24_PCAphaseII_lineage
MEL15	| LSP11322.ome.tif	| HTAN, AWS	| 74.54 GB	| p16_e41_PCAII_tumorintrinsic
MEL16	| LSP11330.ome.tif	| HTAN, AWS	| 278.334 GB |	p16_e41_PCAII_tumorintrinsic
MEL16	| LSP11331.ome.tif |	HTAN, AWS	| 254.785 GB	| RP-p16-e24_PCAphaseII_lineage
MEL17	| LSP11339.ome.tif	| HTAN, AWS |	11.639 GB	| RP-p16-e24_PCAphaseII_lineage
MEL18	| LSP11349.ome.tif	| HTAN, AWS	| 143.981 GB	| p16_e41_PCAII_tumorintrinsic
MEL18	| LSP11347.ome.tif |	HTAN, AWS	| 144.39 GB	| RP-p16-e24_PCAphaseII_lineage
MEL19	| LSP11354.ome.tif |	HTAN, AWS	| 97.876 GB	| p16_e41_PCAII_tumorintrinsic
MEL19	| LSP11355.ome.tif	| HTAN, AWS |	79.282 GB |	RP-p16-e24_PCAphaseII_lineage
MEL21	| LSP11373.ome.tif	| HTAN, AWS	| 67.29 GB |	p16_e41_PCAII_tumorintrinsic
MEL21	| LSP11371.ome.tif	| HTAN, AWS	| 65.799 GB |	RP-p16-e24_PCAphaseII_lineage
MEL22	| LSP11378.ome.tif	| HTAN, AWS	| 705.52 GB |	p16_e41_PCAII_tumorintrinsic
MEL22	| LSP11379.ome.tif	| HTAN, AWS	| 567.648 GB |	RP-p16-e24_PCAphaseII_lineage
MEL23	| LSP11386.ome.tif	| HTAN, AWS	| 451.995 GB |	p16_e41_PCAII_tumorintrinsic
MEL23	| LSP11387.ome.tif	| HTAN, AWS	| 393.297 GB |	RP-p16-e24_PCAphaseII_lineage
MEL24	| LSP11394.ome.tif	| HTAN, AWS	| 67.29 GB |	p16_e41_PCAII_tumorintrinsic
MEL24	| LSP11395.ome.tif	| HTAN, AWS	| 106.823 GB |	RP-p16-e24_PCAphaseII_lineage
MEL25	| LSP11402.ome.tif	| HTAN, AWS	| 154.517 GB |	p16_e41_PCAII_tumorintrinsic
MEL25	| LSP11403.ome.tif	| HTAN, AWS	| 157.181 GB |	RP-p16-e24_PCAphaseII_lineage
MEL26	| LSP11410.ome.tif	| HTAN, AWS	| 84.055 GB |	p16_e41_PCAII_tumorintrinsic
MEL26	| LSP11411.ome.tif	| HTAN, AWS	| 97.374 GB |	RP-p16-e24_PCAphaseII_lineage
MEL27	| LSP11418.ome.tif	| HTAN, AWS	| 244.195 GB |	p16_e41_PCAII_tumorintrinsic
MEL27	| LSP11419.ome.tif	| HTAN, AWS	| 268.959 GB |	RP-p16-e24_PCAphaseII_lineage
MEL28	| LSP11426.ome.tif	| HTAN, AWS	| 35.457 GB |	p16_e41_PCAII_tumorintrinsic
MEL29	| LSP11435.ome.tif	| HTAN, AWS	| 11.408 GB |	RP-p16-e24_PCAphaseII_lineage
MEL30 |	LSP11440.ome.tif	| HTAN, AWS	| 21.428 GB |	p16_e41_PCAII_tumorintrinsic
MEL31 |	LSP11450.ome.tif	| HTAN, AWS	| 75.219 GB |	p16_e41_PCAII_tumorintrinsic
MEL31 |	LSP11451.ome.tif	| HTAN, AWS	| 59.727 GB |	RP-p16-e24_PCAphaseII_lineage
MEL32	| LSP11458.ome.tif	| HTAN, AWS	| 147.153 GB |	p16_e41_PCAII_tumorintrinsic
MEL32	| LSP11459.ome.tif	| HTAN, AWS	| 132.405 GB |	RP-p16-e24_PCAphaseII_lineage
MEL33	| LSP11466.ome.tif	| HTAN, AWS	| 107.505 GB |	p16_e41_PCAII_tumorintrinsic
MEL33 |	LSP11467.ome.tif	| HTAN, AWS	| 109.358 GB |	RP-p16-e24_PCAphaseII_lineage
MEL34	| LSP11474.ome.tif	| HTAN, AWS	| 89.493 GB |	p16_e41_PCAII_tumorintrinsic
MEL34 |	LSP11475.ome.tif	| HTAN, AWS	| 83.776 GB |	RP-p16-e24_PCAphaseII_lineage
MEL35 |	LSP11482.ome.tif	| HTAN, AWS	| 263.607 GB |	p16_e41_PCAII_tumorintrinsic
MEL35 |	LSP11483.ome.tif	| HTAN, AWS	| 285.437 GB |	RP-p16-e24_PCAphaseII_lineage
MEL36 |	LSP11490.ome.tif	| HTAN, AWS	| 79.864 GB	| p16_e41_PCAII_tumorintrinsic
MEL36 |	LSP11498.ome.tif	| HTAN, AWS	| 30.133 GB |	p16_e41_PCAII_tumorintrinsic
MEL37 |	LSP11506.ome.tif	| HTAN, AWS	| 250.58 GB |	p16_e41_PCAII_tumorintrinsic
MEL37 |	LSP11507.ome.tif	| HTAN, AWS	| 230.355 GB |	RP-p16-e24_PCAphaseII_lineage
MEL38 |	LSP11514.ome.tif	| HTAN, AWS	| 137.864 GB |	p16_e41_PCAII_tumorintrinsic
MEL38 |	LSP11515.ome.tif	| HTAN, AWS	| 110.971 GB |	RP-p16-e24_PCAphaseII_lineage
MEL39 |	LSP11522.ome.tif	| HTAN, AWS	| 43.614 GB	| p16_e41_PCAII_tumorintrinsic
MEL39 |	LSP11523.ome.tif	| HTAN, AWS	| 24.891 GB |	RP-p16-e24_PCAphaseII_lineage
MEL40 |	LSP11530.ome.tif	| HTAN, AWS	| 141.942 GB |	p16_e41_PCAII_tumorintrinsic
MEL40	| LSP11531.ome.tif | HTAN, AWS	| 106.823 GB |	RP-p16-e24_PCAphaseII_lineage
MEL41 |	LSP11538.ome.tif |	HTAN, AWS	| 105.919 GB | p16_e41_PCAII_tumorintrinsic
MEL42 |	LSP11546.ome.tif |	HTAN, AWS |	76.638 GB	| p16_e41_PCAII_tumorintrinsic
MEL42 |	LSP11547.ome.tif |	HTAN, AWS |	175.958 GB |	RP-p16-e24_PCAphaseII_lineage
MEL44 |	LSP11562.ome.tif	| HTAN, AWS	| 39.082 GB |	p16_e41_PCAII_tumorintrinsic
MEL44 |	LSP11563.ome.tif	| HTAN, AWS	| 95.069 GB |	RP-p16-e24_PCAphaseII_lineage
MEL45 |	LSP11570.ome.tif	| HTAN, AWS	| 34.481 GB |	p16_e41_PCAII_tumorintrinsic
MEL45 |	LSP11571.ome.tif |	HTAN, AWS |	69.256 GB |	RP-p16-e24_PCAphaseII_lineage
MEL47 |	LSP11586.ome.tif	| HTAN, AWS	| 35.23 GB |	p16_e41_PCAII_tumorintrinsic
MEL47 |	LSP11587.ome.tif	| HTAN, AWS	| 50.243 GB |	RP-p16-e24_PCAphaseII_lineage
MEL48 |	LSP11594.ome.tif | HTAN, AWS	| 42.303 GB |	p16_e41_PCAII_tumorintrinsic
MEL48 |	LSP11595.ome.tif	| HTAN, AWS	| 59.692 GB |	RP-p16-e24_PCAphaseII_lineage
MEL49 |	LSP11602.ome.tif |	HTAN, AWS	| 166.978 GB |	p16_e41_PCAII_tumorintrinsic
MEL49 |	LSP11603.ome.tif	| HTAN, AWS	| 95.069 GB |	RP-p16-e24_PCAphaseII_lineage
MEL50	| LSP12424.ome.tif	| HTAN, AWS	| 154.517 GB |	p16_e41_PCAII_tumorintrinsic
MEL50 |	LSP12422.ome.tif	| HTAN, AWS	| 138.397 GB |	RP-p16-e24_PCAphaseII_lineage
MEL51 |	LSP11618.ome.tif	| HTAN, AWS	| 105.012 GB |	p16_e41_PCAII_tumorintrinsic
MEL52 |	LSP11626.ome.tif	| HTAN, AWS	| 28.321 GB	| p16_e41_PCAII_tumorintrinsic
MEL52 |	LSP11627.ome.tif	| HTAN, AWS |	120.536 GB |	RP-p16-e24_PCAphaseII_lineage
MEL53	| LSP11634.ome.tif	| HTAN, AWS	| 280.599 GB |	p16_e41_PCAII_tumorintrinsic
MEL53	| LSP11635.ome.tif	| HTAN, AWS	| 229.433 GB |	RP-p16-e24_PCAphaseII_lineage
MEL54	| LSP11642.ome.tif	| HTAN, AWS	| 496.288 GB |	p16_e41_PCAII_tumorintrinsic
MEL54	| LSP11643.ome.tif	| HTAN, AWS |	446.305 GB |	RP-p16-e24_PCAphaseII_lineage
MEL55	| LSP11658.ome.tif	| HTAN, AWS	| 242.537 GB |	p16_e41_PCAII_tumorintrinsic
MEL55	| LSP11659.ome.tif	| HTAN, AWS	| 198.435 GB |	RP-p16-e24_PCAphaseII_lineage
MEL56 |	LSP11667.ome.tif	| HTAN, AWS	| 65.223 GB |	RP-p16-e24_PCAphaseII_lineage
MEL58 | LSP11690.ome.tif	| HTAN, AWS	| 225.544 GB |	p16_e41_PCAII_tumorintrinsic
MEL58	| LSP11691.ome.tif	| HTAN, AWS	| 217.333 GB |	RP-p16-e24_PCAphaseII_lineage
MEL59 |	LSP11698.ome.tif	| HTAN, AWS	| 100.028 GB |	p16_e41_PCAII_tumorintrinsic
MEL60	| LSP11706.ome.tif	| HTAN, AWS	| 92.438 GB |	p16_e41_PCAII_tumorintrinsic
MEL60	| LSP11707.ome.tif	| HTAN, AWS	| 68.911 GB |	RP-p16-e24_PCAphaseII_lineage
MEL61 |	LSP11714.ome.tif	| HTAN, AWS	| 520.79 GB |	p16_e41_PCAII_tumorintrinsic
MEL62	| LSP11720.ome.tif	| HTAN, AWS	| 17.445 GB |	p16_e41_PCAII_tumorintrinsic
MEL64	| LSP11738.ome.tif	| HTAN, AWS	| 189.521 GB |	p16_e41_PCAII_tumorintrinsic
MEL64	| LSP11739.ome.tif	| HTAN, AWS	| 173.314 GB |	RP-p16-e24_PCAphaseII_lineage
MEL65	| LSP11746.ome.tif	| HTAN, AWS	| 93.061 GB |	p16_e41_PCAII_tumorintrinsic
MEL65	| LSP11747.ome.tif	| HTAN, AWS	| 116.272 GB |	RP-p16-e24_PCAphaseII_lineage
MEL66	| LSP11754.ome.tif	| HTAN, AWS	| 22.883 GB |	p16_e41_PCAII_tumorintrinsic
MEL67	| LSP11762.ome.tif	| HTAN, AWS	| 46.982 GB |	p16_e41_PCAII_tumorintrinsic
MEL68	| LSP11770.ome.tif	| HTAN, AWS	| 52.411 GB |	p16_e41_PCAII_tumorintrinsic
MEL68	| LSP11778.ome.tif	| HTAN, AWS	| 87.794 GB |	p16_e41_PCAII_tumorintrinsic
MEL68	| LSP11771.ome.tif	| HTAN, AWS	| 117.77 GB | RP-p16-e24_PCAphaseII_lineage
MEL69	| LSP11786.ome.tif	| HTAN, AWS	| 89.493 GB |	p16_e41_PCAII_tumorintrinsic
MEL70 |	LSP13078.ome.tif	| HTAN, AWS	| 777.149 GB |	p135_e9_PCAlineage
MEL71	| LSP13179.ome.tif	| HTAN, AWS	| 1.114 TB |	p135_e9_PCAlineage
MEL72	| LSP13186.ome.tif	| HTAN, AWS	| 633.195 GB |	p135_e9_PCAlineage
MEL73	| LSP13102.ome.tif	| HTAN, AWS	| 838.864 GB |	p135_e9_PCAlineage
MEL74	| LSP15120.ome.tif	| HTAN, AWS	| 701.27 GB |	p135_e9_PCAlineage
MEL75	| LSP15129.ome.tif	| HTAN, AWS	| 960.967 GB |	p135_e9_PCAlineage
MEL76	| LSP15138.ome.tif	| HTAN, AWS	| 294.99 GB |	p135_e9_PCAlineage
MEL78	| LSP15156.ome.tif	| HTAN, AWS	| 759.372 GB |	p135_e9_PCAlineage
MEL79	| LSP15165.ome.tif	| HTAN, AWS	| 205.894 GB |	p135_e9_PCAlineage
MEL80	| LSP15174.ome.tif	| HTAN, AWS	| 429.22 GB |	p135_e9_PCAlineage
MEL81	| LSP15183.ome.tif	| HTAN, AWS	| 382.866 GB |	p135_e9_PCAlineage
MEL82	| LSP15192.ome.tif	| HTAN, AWS	| 836.14 GB |	p135_e9_PCAlineage
MEL83	| LSP15201.ome.tif	| HTAN, AWS	| 436.053 GB |	p135_e9_PCAlineage
MEL84	| LSP15210.ome.tif	| HTAN, AWS	| 236.744 GB |	p135_e9_PCAlineage
MEL85/MEL86	| LSP15219.ome.tif	| HTAN, AWS | 375.639 GB |	p135_e9_PCAlineage |

​
​
### H&E Image Data
|Patient ID | File Name      | Location| File size|
|--------| ---------------|---------|----------|
MEL14	|	LSP11311.ome.tif	|	HTAN, AWS	|	17.107 GB	|
MEL15	|	LSP11319.ome.tif	|	HTAN, AWS	|	5.78 GB	|
MEL16	|	LSP11327.ome.tif	|	HTAN, AWS	|	8.376 GB	|
MEL17	|	LSP11335.ome.tif	|	HTAN, AWS	|	2.065 GB	|
MEL18	|	LSP11343.ome.tif	|	HTAN, AWS	|	4.298 GB	|
MEL19	|	LSP11351.ome.tif	|	HTAN, AWS	|	2.915 GB	|
MEL21	|	LSP11367.ome.tif	|	HTAN, AWS	|	3.214 GB	|
MEL22	|	LSP11375.ome.tif	|	HTAN, AWS	|	18.95 GB	|
MEL23	|	LSP11383.ome.tif	|	HTAN, AWS	|	10.828 GB	|
MEL24	|	LSP11391.ome.tif	|	HTAN, AWS	|	3.135 GB	|
MEL25	|	LSP11399.ome.tif	|	HTAN, AWS	|	3.996 GB	|
MEL26	|	LSP11407.ome.tif	|	HTAN, AWS	|	3.234 GB	|
MEL27	|	LSP11415.ome.tif	|	HTAN, AWS	|	9.422 GB	|
MEL28	|	LSP11423.ome.tif	|	HTAN, AWS	|	6.639 GB	|
MEL29	|	LSP11431.ome.tif	|	HTAN, AWS	|	387.0 MB	|
MEL30	|	LSP11439.ome.tif	|	HTAN, AWS	|	4.846 GB	|
MEL31	|	LSP11447.ome.tif	|	HTAN, AWS	|	2.092 GB	|
MEL32	|	LSP11455.ome.tif	|	HTAN, AWS	|	7.532 GB	|
MEL33	|	LSP11463.ome.tif	|	HTAN, AWS	|	7.655 GB	|
MEL34	|	LSP11471.ome.tif	|	HTAN, AWS	|	2.285 GB	|
MEL35	|	LSP11479.ome.tif	|	HTAN, AWS	|	8.001 GB	|
MEL36	|	LSP11487.ome.tif	|	HTAN, AWS	|	2.994 GB	|
MEL36	|	LSP11495.ome.tif	|	HTAN, AWS	|	1.43 GB	|
MEL37	|	LSP11503.ome.tif	|	HTAN, AWS	|	6.035 GB	|
MEL38	|	LSP11511.ome.tif	|	HTAN, AWS	|	14.414 GB	|
MEL39	|	LSP11519.ome.tif	|	HTAN, AWS	|	1.128 GB	|
MEL40	|	LSP11527.ome.tif	|	HTAN, AWS	|	3.413 GB	|
MEL41	|	LSP11535.ome.tif	|	HTAN, AWS	|	3.413 GB	|
MEL42	|	LSP11543.ome.tif	|	HTAN, AWS	|	10.07 GB	|
MEL44	|	LSP11559.ome.tif	|	HTAN, AWS	|	2.675 GB	|
MEL45	|	LSP11567.ome.tif	|	HTAN, AWS	|	2.314 GB	|
MEL47	|	LSP11583.ome.tif	|	HTAN, AWS	|	2.314 GB	|
MEL48	|	LSP11591.ome.tif	|	HTAN, AWS	|	4.061 GB	|
MEL49	|	LSP11599.ome.tif	|	HTAN, AWS	|	5.432 GB	|
MEL51	|	LSP11615.ome.tif	|	HTAN, AWS	|	3.677 GB	|
MEL52	|	LSP11623.ome.tif	|	HTAN, AWS	|	6.375 GB	|
MEL53	|	LSP11631.ome.tif	|	HTAN, AWS	|	8.728 GB	|
MEL54	|	LSP11639.ome.tif	|	HTAN, AWS	|	18.337 GB	|
MEL55	|	LSP11655.ome.tif	|	HTAN, AWS	|	6.513 GB	|
MEL56	|	LSP11663.ome.tif	|	HTAN, AWS	|	2.543 GB	|
MEL58	|	LSP11687.ome.tif	|	HTAN, AWS	|	7.257 GB	|
MEL59	|	LSP11695.ome.tif	|	HTAN, AWS	|	3.565 GB	|
MEL60	|	LSP11703.ome.tif	|	HTAN, AWS	|	3.908 GB	|
MEL61	|	LSP11711.ome.tif	|	HTAN, AWS	|	17.854 GB	|
MEL62	|	LSP11719.ome.tif	|	HTAN, AWS	|	1.087 GB	|
MEL64	|	LSP11735.ome.tif	|	HTAN, AWS	|	7.236 GB	|
MEL65	|	LSP11743.ome.tif	|	HTAN, AWS	|	5.045 GB	|
MEL66	|	LSP11751.ome.tif	|	HTAN, AWS	|	1.374 GB	|
MEL67	|	LSP11759.ome.tif	|	HTAN, AWS	|	4.878 GB	|
MEL68	|	LSP11767.ome.tif	|	HTAN, AWS	|	3.671 GB	|
MEL68	|	LSP11775.ome.tif	|	HTAN, AWS	|	6.278 GB	|
MEL69	|	LSP11783.ome.tif	|	HTAN, AWS	|	4.061 GB	|
MEL50 	|	LSP12427.ome.tif	|	HTAN, AWS	|	5.525 GB	|
MEL70	|	LSP13074_20220526_202440_361948.ome.tiff	|	HTAN, AWS	|	19.208 GB	|
MEL71	|	LSP13082_20220526_202440_397948.ome.tiff	|	HTAN, AWS	|	27.177 GB	|
MEL72	|	LSP13090_20220526_202440_378948.ome.tiff	|	HTAN, AWS	|	22.75 GB	|
MEL73	|	LSP13098_20220526_202440_345948.ome.tiff	|	HTAN, AWS	|	19.773 GB	|
MEL74	|	LSP17553.ome.tif	|	HTAN, AWS	|	4.52 GB	|
MEL75	|	LSP17557.ome.tif	|	HTAN, AWS	|	6.296 GB	|
MEL76	|	LSP17561.ome.tif	|	HTAN, AWS	|	2.946 GB	|
MEL77	|	LSP17565.ome.tif	|	HTAN, AWS	|	4.064 GB	|
MEL78	|	LSP17569.ome.tif	|	HTAN, AWS	|	3.608 GB	|
MEL79	|	LSP17573.ome.tif	|	HTAN, AWS	|	2.345 GB	|
MEL80	|	LSP17577.ome.tif	|	HTAN, AWS	|	1.444 GB	|
MEL81	|	LSP17581.ome.tif	|	HTAN, AWS	|	1.939 GB	|
MEL82	|	LSP17585.ome.tif	|	HTAN, AWS	|	6.256 GB	|
MEL83	|	LSP17589.ome.tif	|	HTAN, AWS	|	3.114 GB	|
MEL84	|	LSP17593.ome.tif	|	HTAN, AWS	|	1.188 GB	|
MEL85/MEL86	|	LSP17597.ome.tif	|	HTAN, AWS	|	1.214 GB	|


​
### Segmentation Mask Data
|Patient ID | File Name      | Location | File size | CyCIF Panel |
|--------| ---------------|---------|----------|--------|
MEL14	|	LSP11314-mask-cell.ome.tif	|	HTAN, AWS	|	14.343 GB	|	p16_e41_PCAII_tumorintrinsic
MEL14	|	LSP11315-mask-cell.ome.tif	|	HTAN, AWS	|	11.994 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL15	|	LSP11322-mask-cell.ome.tif	|	HTAN, AWS	|	2.233 GB	|	p16_e41_PCAII_tumorintrinsic
MEL16	|	LSP11330-mask-cell.ome.tif	|	HTAN, AWS	|	9.368 GB	|	p16_e41_PCAII_tumorintrinsic
MEL16	|	LSP11331-mask-cell.ome.tif	|	HTAN, AWS	|	8.421 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL17	|	LSP11339-mask-cell.ome.tif	|	HTAN, AWS	|	329.7 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL18	|	LSP11347-mask-cell.ome.tif	|	HTAN, AWS	|	4.832 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL18	|	LSP11349-mask-cell.ome.tif	|	HTAN, AWS	|	4.761 GB	|	p16_e41_PCAII_tumorintrinsic
MEL19	|	LSP11354-mask-cell.ome.tif	|	HTAN, AWS	|	3.126 GB	|	p16_e41_PCAII_tumorintrinsic
MEL19	|	LSP11355-mask-cell.ome.tif	|	HTAN, AWS	|	2.578 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL21	|	LSP11371-mask-cell.ome.tif	|	HTAN, AWS	|	2.187 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL21	|	LSP11373-mask-cell.ome.tif	|	HTAN, AWS	|	2.105 GB	|	p16_e41_PCAII_tumorintrinsic
MEL22	|	LSP11378-mask-cell.ome.tif	|	HTAN, AWS	|	23.788 GB	|	p16_e41_PCAII_tumorintrinsic
MEL22	|	LSP11379-mask-cell.ome.tif	|	HTAN, AWS	|	19.1 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL23	|	LSP11386-mask-cell.ome.tif	|	HTAN, AWS	|	15.457 GB	|	p16_e41_PCAII_tumorintrinsic
MEL23	|	LSP11387-mask-cell.ome.tif	|	HTAN, AWS	|	13.218 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL24	|	LSP11394-mask-cell.ome.tif	|	HTAN, AWS	|	2.169 GB	|	p16_e41_PCAII_tumorintrinsic
MEL24	|	LSP11395-mask-cell.ome.tif	|	HTAN, AWS	|	3.444 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL25	|	LSP11402-mask-cell.ome.tif	|	HTAN, AWS	|	5.203 GB	|	p16_e41_PCAII_tumorintrinsic
MEL25	|	LSP11403-mask-cell.ome.tif	|	HTAN, AWS	|	5.203 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL26	|	LSP11410-mask-cell.ome.tif	|	HTAN, AWS	|	2.662 GB	|	p16_e41_PCAII_tumorintrinsic
MEL26	|	LSP11411-mask-cell.ome.tif	|	HTAN, AWS	|	3.165 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL27	|	LSP11418-mask-cell.ome.tif	|	HTAN, AWS	|	8.951 GB	|	p16_e41_PCAII_tumorintrinsic
MEL27	|	LSP11419-mask-cell.ome.tif	|	HTAN, AWS	|	8.863 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL28	|	LSP11426-mask-cell.ome.tif	|	HTAN, AWS	|	1.074 GB	|	p16_e41_PCAII_tumorintrinsic
MEL29	|	LSP11435-mask-cell.ome.tif	|	HTAN, AWS	|	333.0 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL30	|	LSP11440-mask-cell.ome.tif	|	HTAN, AWS	|	772.6 MB	|	p16_e41_PCAII_tumorintrinsic
MEL31	|	LSP11450-mask-cell.ome.tif	|	HTAN, AWS	|	2.415 GB	|	p16_e41_PCAII_tumorintrinsic
MEL31	|	LSP11451-mask-cell.ome.tif	|	HTAN, AWS	|	2.07 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL32	|	LSP11458-mask-cell.ome.tif	|	HTAN, AWS	|	4.765 GB	|	p16_e41_PCAII_tumorintrinsic
MEL32	|	LSP11459-mask-cell.ome.tif	|	HTAN, AWS	|	4.225 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL33	|	LSP11466-mask-cell.ome.tif	|	HTAN, AWS	|	3.603 GB	|	p16_e41_PCAII_tumorintrinsic
MEL33	|	LSP11467-mask-cell.ome.tif	|	HTAN, AWS	|	3.603 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL34	|	LSP11474-mask-cell.ome.tif	|	HTAN, AWS	|	2.87 GB	|	p16_e41_PCAII_tumorintrinsic
MEL34	|	LSP11475-mask-cell.ome.tif	|	HTAN, AWS	|	2.615 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL35	|	LSP11482-mask-cell.ome.tif	|	HTAN, AWS	|	8.832 GB	|	p16_e41_PCAII_tumorintrinsic
MEL35	|	LSP11483-mask-cell.ome.tif	|	HTAN, AWS	|	9.434 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL36	|	LSP11490-mask-cell.ome.tif	|	HTAN, AWS	|	2.601 GB	|	p16_e41_PCAII_tumorintrinsic
MEL36	|	LSP11498-mask-cell.ome.tif	|	HTAN, AWS	|	913.9 MB	|	p16_e41_PCAII_tumorintrinsic
MEL37	|	LSP11506-mask-cell.ome.tif	|	HTAN, AWS	|	8.531 GB	|	p16_e41_PCAII_tumorintrinsic
MEL37	|	LSP11507-mask-cell.ome.tif	|	HTAN, AWS	|	7.618 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL38	|	LSP11514-mask-cell.ome.tif	|	HTAN, AWS	|	4.632 GB	|	p16_e41_PCAII_tumorintrinsic
MEL38	|	LSP11515-mask-cell.ome.tif	|	HTAN, AWS	|	3.629 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL39	|	LSP11522-mask-cell.ome.tif	|	HTAN, AWS	|	1.34 GB	|	p16_e41_PCAII_tumorintrinsic
MEL39	|	LSP11523-mask-cell.ome.tif	|	HTAN, AWS	|	744.6 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL40	|	LSP11530-mask-cell.ome.tif	|	HTAN, AWS	|	4.832 GB	|	p16_e41_PCAII_tumorintrinsic
MEL40	|	LSP11531-mask-cell.ome.tif	|	HTAN, AWS	|	3.444 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL41	|	LSP11538-mask-cell.ome.tif	|	HTAN, AWS	|	3.456 GB	|	p16_e41_PCAII_tumorintrinsic
MEL42	|	LSP11546-mask-cell.ome.tif	|	HTAN, AWS	|	5.165 GB	|	p16_e41_PCAII_tumorintrinsic
MEL42	|	LSP11547-mask-cell.ome.tif	|	HTAN, AWS	|	6.297 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL44	|	LSP11562-mask-cell.ome.tif	|	HTAN, AWS	|	1.167 GB	|	p16_e41_PCAII_tumorintrinsic
MEL44	|	LSP11563-mask-cell.ome.tif	|	HTAN, AWS	|	3.083 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL45	|	LSP11570-mask-cell.ome.tif	|	HTAN, AWS	|	2.615 GB	|	p16_e41_PCAII_tumorintrinsic
MEL45	|	LSP11571-mask-cell.ome.tif	|	HTAN, AWS	|	2.226 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL47	|	LSP11586-mask-cell.ome.tif	|	HTAN, AWS	|	2.285 GB	|	p16_e41_PCAII_tumorintrinsic
MEL47	|	LSP11587-mask-cell.ome.tif	|	HTAN, AWS	|	1.601 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL48	|	LSP11594-mask-cell.ome.tif	|	HTAN, AWS	|	2.691 GB	|	p16_e41_PCAII_tumorintrinsic
MEL48	|	LSP11595-mask-cell.ome.tif	|	HTAN, AWS	|	1.914 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL49	|	LSP11602-mask-cell.ome.tif	|	HTAN, AWS	|	5.585 GB	|	p16_e41_PCAII_tumorintrinsic
MEL49	|	LSP11603-mask-cell.ome.tif	|	HTAN, AWS	|	3.083 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL51	|	LSP11618-mask-cell.ome.tif	|	HTAN, AWS	|	3.444 GB	|	p16_e41_PCAII_tumorintrinsic
MEL52	|	LSP11626-mask-cell.ome.tif	|	HTAN, AWS	|	906.7 MB	|	p16_e41_PCAII_tumorintrinsic
MEL52	|	LSP11627-mask-cell.ome.tif	|	HTAN, AWS	|	4.01 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL53	|	LSP11634-mask-cell.ome.tif	|	HTAN, AWS	|	9.434 GB	|	p16_e41_PCAII_tumorintrinsic
MEL53	|	LSP11635-mask-cell.ome.tif	|	HTAN, AWS	|	7.656 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL54	|	LSP11642-mask-cell.ome.tif	|	HTAN, AWS	|	16.999 GB	|	p16_e41_PCAII_tumorintrinsic
MEL54	|	LSP11643-mask-cell.ome.tif	|	HTAN, AWS	|	14.999 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL55	|	LSP11658-mask-cell.ome.tif	|	HTAN, AWS	|	8.107 GB	|	p16_e41_PCAII_tumorintrinsic
MEL55	|	LSP11659-mask-cell.ome.tif	|	HTAN, AWS	|	6.609 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL56	|	LSP11667-mask-cell.ome.tif	|	HTAN, AWS	|	2.05 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL58	|	LSP11690-mask-cell.ome.tif	|	HTAN, AWS	|	7.566 GB	|	p16_e41_PCAII_tumorintrinsic
MEL58	|	LSP11691-mask-cell.ome.tif	|	HTAN, AWS	|	7.218 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL59	|	LSP11698-mask-cell.ome.tif	|	HTAN, AWS	|	3.32 GB	|	p16_e41_PCAII_tumorintrinsic
MEL60	|	LSP11706-mask-cell.ome.tif	|	HTAN, AWS	|	2.967 GB	|	p16_e41_PCAII_tumorintrinsic
MEL60	|	LSP11707-mask-cell.ome.tif	|	HTAN, AWS	|	2.265 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL61	|	LSP11714-mask-cell.ome.tif	|	HTAN, AWS	|	19.632 GB	|	p16_e41_PCAII_tumorintrinsic
MEL62	|	LSP11720-mask-cell.ome.tif	|	HTAN, AWS	|	546.1 MB	|	p16_e41_PCAII_tumorintrinsic
MEL64	|	LSP11738-mask-cell.ome.tif	|	HTAN, AWS	|	6.359 GB	|	p16_e41_PCAII_tumorintrinsic
MEL64	|	LSP11739-mask-cell.ome.tif	|	HTAN, AWS	|	5.713 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL65	|	LSP11746-mask-cell.ome.tif	|	HTAN, AWS	|	3.397 GB	|	p16_e41_PCAII_tumorintrinsic
MEL65	|	LSP11747-mask-cell.ome.tif	|	HTAN, AWS	|	3.686 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL66	|	LSP11754-mask-cell.ome.tif	|	HTAN, AWS	|	685.3 MB	|	p16_e41_PCAII_tumorintrinsic
MEL67	|	LSP11762-mask-cell.ome.tif	|	HTAN, AWS	|	3.165 GB	|	p16_e41_PCAII_tumorintrinsic
MEL68	|	LSP11770-mask-cell.ome.tif	|	HTAN, AWS	|	3.456 GB	|	p16_e41_PCAII_tumorintrinsic
MEL68	|	LSP11771-mask-cell.ome.tif	|	HTAN, AWS	|	3.84 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL68	|	LSP11778-mask-cell.ome.tif	|	HTAN, AWS	|	2.792 GB	|	p16_e41_PCAII_tumorintrinsic
MEL69	|	LSP11786-mask-cell.ome.tif	|	HTAN, AWS	|	2.87 GB	|	p16_e41_PCAII_tumorintrinsic
MEL50	|	LSP12422-mask-cell.ome.tif	|	HTAN, AWS	|	4.451 GB	|	RP-p16-e24_PCAphaseII_lineage
MEL50	|	LSP12424-mask-cell.ome.tif	|	HTAN, AWS	|	5.142 GB	|	p16_e41_PCAII_tumorintrinsic
MEL70	|	LSP13078-mask-cell.ome.tif	|	HTAN, AWS	|	20.733 GB	|	p135_e9_PCAlineage
MEL73	|	LSP13102-mask-cell.ome.tif	|	HTAN, AWS	|	22.392 GB	|	p135_e9_PCAlineage
MEL71	|	LSP13179-mask-cell.ome.tif	|	HTAN, AWS	|	28.408 GB	|	p135_e9_PCAlineage
MEL72	|	LSP13186-mask-cell.ome.tif	|	HTAN, AWS	|	16.999 GB	|	p135_e9_PCAlineage
MEL74	|	LSP15120-mask-cell.ome.tif	|	HTAN, AWS	|	18.845 GB	|	p135_e9_PCAlineage
MEL75	|	LSP15129-mask-cell.ome.tif	|	HTAN, AWS	|	23.788 GB	|	p135_e9_PCAlineage
MEL76	|	LSP15138-mask-cell.ome.tif	|	HTAN, AWS	|	7.782 GB	|	p135_e9_PCAlineage
MEL78	|	LSP15156-mask-cell.ome.tif	|	HTAN, AWS	|	20.268 GB	|	p135_e9_PCAlineage
MEL79	|	LSP15165-mask-cell.ome.tif	|	HTAN, AWS	|	10.406 GB	|	p135_e9_PCAlineage
MEL80	|	LSP15174-mask-cell.ome.tif	|	HTAN, AWS	|	5.945 GB	|	p135_e9_PCAlineage
MEL81	|	LSP15183-mask-cell.ome.tif	|	HTAN, AWS	|	10.14 GB	|	p135_e9_PCAlineage
MEL82	|	LSP15192-mask-cell.ome.tif	|	HTAN, AWS	|	20.939 GB	|	p135_e9_PCAlineage
MEL83	|	LSP15201-mask-cell.ome.tif	|	HTAN, AWS	|	11.666 GB	|	p135_e9_PCAlineage
MEL84	|	LSP15210-mask-cell.ome.tif	|	HTAN, AWS	|	6.297 GB	|	p135_e9_PCAlineage
MEL85/MEL86	|	LSP15219-mask-cell.ome.tif	|	HTAN, AWS	|	9.877 GB	|	p135_e9_PCAlineage


​

### Features Table Data
|Patient ID | File Name      | Location | File size | CyCIF Panel |
|------- | ------------|------------|-----------|-------|
MEL14	|	LSP11314--unmicst_cellRing.csv	|	HTAN, AWS	|	128.5 MB	|	p16_e41_PCAII_tumorintrinsic
MEL14	|	unmicst-LSP11315_cell.csv	|	HTAN, AWS	|	141.2 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL15	|	LSP11322--unmicst_cellRing.csv	|	HTAN, AWS	|	31.2 MB	|	p16_e41_PCAII_tumorintrinsic
MEL16	|	LSP11330--unmicst_cellRing.csv	|	HTAN, AWS	|	128.8 MB	|	p16_e41_PCAII_tumorintrinsic
MEL16	|	unmicst-LSP11331_cell.csv	|	HTAN, AWS	|	96.9 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL17	|	unmicst-LSP11339_cell.csv	|	HTAN, AWS	|	12.6 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL18	|	unmicst-LSP11347_cell.csv	|	HTAN, AWS	|	131.5 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL18	|	LSP11349--unmicst_cellRing.csv	|	HTAN, AWS	|	128.7 MB	|	p16_e41_PCAII_tumorintrinsic
MEL19	|	LSP11354--unmicst_cellRing.csv	|	HTAN, AWS	|	104.1 MB	|	p16_e41_PCAII_tumorintrinsic
MEL19	|	unmicst-LSP11355_cell.csv	|	HTAN, AWS	|	83.9 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL21	|	unmicst-LSP11371_cell.csv	|	HTAN, AWS	|	13.8 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL21	|	LSP11373--unmicst_cellRing.csv	|	HTAN, AWS	|	29.0 MB	|	p16_e41_PCAII_tumorintrinsic
MEL22	|	LSP11378--unmicst_cellRing.csv	|	HTAN, AWS	|	286.8 MB	|	p16_e41_PCAII_tumorintrinsic
MEL22	|	unmicst-LSP11379_cell.csv	|	HTAN, AWS	|	290.9 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL23	|	LSP11386--unmicst_cellRing.csv	|	HTAN, AWS	|	245.2 MB	|	p16_e41_PCAII_tumorintrinsic
MEL23	|	unmicst-LSP11387_cell.csv	|	HTAN, AWS	|	243.5 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL24	|	LSP11394--unmicst_cellRing.csv	|	HTAN, AWS	|	34.3 MB	|	p16_e41_PCAII_tumorintrinsic
MEL24	|	unmicst-LSP11395_cell.csv	|	HTAN, AWS	|	67.1 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL25	|	LSP11402--unmicst_cellRing.csv	|	HTAN, AWS	|	112.3 MB	|	p16_e41_PCAII_tumorintrinsic
MEL25	|	unmicst-LSP11403_cell.csv	|	HTAN, AWS	|	116.4 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL26	|	LSP11410--unmicst_cellRing.csv	|	HTAN, AWS	|	39.3 MB	|	p16_e41_PCAII_tumorintrinsic
MEL26	|	unmicst-LSP11411_cell.csv	|	HTAN, AWS	|	58.2 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL27	|	LSP11418--unmicst_cellRing.csv	|	HTAN, AWS	|	132.5 MB	|	p16_e41_PCAII_tumorintrinsic
MEL27	|	unmicst-LSP11419_cell.csv	|	HTAN, AWS	|	145.9 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL28	|	LSP11426--unmicst_cellRing.csv	|	HTAN, AWS	|	9.0 MB	|	p16_e41_PCAII_tumorintrinsic
MEL29	|	unmicst-LSP11435_cell.csv	|	HTAN, AWS	|	3.8 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL30	|	LSP11440--unmicst_cellRing.csv	|	HTAN, AWS	|	16.5 MB	|	p16_e41_PCAII_tumorintrinsic
MEL31	|	LSP11450--unmicst_cellRing.csv	|	HTAN, AWS	|	37.1 MB	|	p16_e41_PCAII_tumorintrinsic
MEL31	|	unmicst-LSP11451_cell.csv	|	HTAN, AWS	|	24.5 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL32	|	LSP11458--unmicst_cellRing.csv	|	HTAN, AWS	|	38.4 MB	|	p16_e41_PCAII_tumorintrinsic
MEL32	|	unmicst-LSP11459_cell.csv	|	HTAN, AWS	|	25.3 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL33	|	LSP11466--unmicst_cellRing.csv	|	HTAN, AWS	|	50.3 MB	|	p16_e41_PCAII_tumorintrinsic
MEL33	|	unmicst-LSP11467_cell.csv	|	HTAN, AWS	|	50.7 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL34	|	LSP11474--unmicst_cellRing.csv	|	HTAN, AWS	|	47.2 MB	|	p16_e41_PCAII_tumorintrinsic
MEL34	|	unmicst-LSP11475_cell.csv	|	HTAN, AWS	|	34.9 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL35	|	LSP11482--unmicst_cellRing.csv	|	HTAN, AWS	|	81.8 MB	|	p16_e41_PCAII_tumorintrinsic
MEL35	|	unmicst-LSP11483_cell.csv	|	HTAN, AWS	|	76.3 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL36	|	LSP11490--unmicst_cellRing.csv	|	HTAN, AWS	|	19.4 MB	|	p16_e41_PCAII_tumorintrinsic
MEL36	|	LSP11498--unmicst_cellRing.csv	|	HTAN, AWS	|	11.9 MB	|	p16_e41_PCAII_tumorintrinsic
MEL37	|	LSP11506--unmicst_cellRing.csv	|	HTAN, AWS	|	58.8 MB	|	p16_e41_PCAII_tumorintrinsic
MEL37	|	unmicst-LSP11507_cell.csv	|	HTAN, AWS	|	46.1 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL38	|	LSP11514--unmicst_cellRing.csv	|	HTAN, AWS	|	60.3 MB	|	p16_e41_PCAII_tumorintrinsic
MEL38	|	unmicst-LSP11515_cell.csv	|	HTAN, AWS	|	34.3 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL39	|	LSP11522--unmicst_cellRing.csv	|	HTAN, AWS	|	15.8 MB	|	p16_e41_PCAII_tumorintrinsic
MEL39	|	unmicst-LSP11523_cell.csv	|	HTAN, AWS	|	16.7 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL40	|	LSP11530--unmicst_cellRing.csv	|	HTAN, AWS	|	51.5 MB	|	p16_e41_PCAII_tumorintrinsic
MEL40	|	unmicst-LSP11531_cell.csv	|	HTAN, AWS	|	44.6 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL41	|	LSP11538--unmicst_cellRing.csv	|	HTAN, AWS	|	66.0 MB	|	p16_e41_PCAII_tumorintrinsic
MEL42	|	LSP11546--unmicst_cellRing.csv	|	HTAN, AWS	|	49.4 MB	|	p16_e41_PCAII_tumorintrinsic
MEL42	|	unmicst-LSP11547_cell.csv	|	HTAN, AWS	|	34.0 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL44	|	LSP11562--unmicst_cellRing.csv	|	HTAN, AWS	|	26.5 MB	|	p16_e41_PCAII_tumorintrinsic
MEL44	|	unmicst-LSP11563_cell.csv	|	HTAN, AWS	|	38.3 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL45	|	LSP11570--unmicst_cellRing.csv	|	HTAN, AWS	|	40.9 MB	|	p16_e41_PCAII_tumorintrinsic
MEL45	|	unmicst-LSP11571_cell.csv	|	HTAN, AWS	|	17.8 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL47	|	LSP11586--unmicst_cellRing.csv	|	HTAN, AWS	|	85.9 MB	|	p16_e41_PCAII_tumorintrinsic
MEL47	|	unmicst-LSP11587_cell.csv	|	HTAN, AWS	|	58.6 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL48	|	LSP11594--unmicst_cellRing.csv	|	HTAN, AWS	|	69.8 MB	|	p16_e41_PCAII_tumorintrinsic
MEL48	|	unmicst-LSP11595_cell.csv	|	HTAN, AWS	|	66.1 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL49	|	LSP11602--unmicst_cellRing.csv	|	HTAN, AWS	|	69.3 MB	|	p16_e41_PCAII_tumorintrinsic
MEL49	|	unmicst-LSP11603_cell.csv	|	HTAN, AWS	|	59.4 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL51	|	LSP11618--unmicst_cellRing.csv	|	HTAN, AWS	|	76.4 MB	|	p16_e41_PCAII_tumorintrinsic
MEL52	|	LSP11626--unmicst_cellRing.csv	|	HTAN, AWS	|	46.5 KB	|	p16_e41_PCAII_tumorintrinsic
MEL52	|	unmicst-LSP11627_cell.csv	|	HTAN, AWS	|	52.9 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL53	|	LSP11634--unmicst_cellRing.csv	|	HTAN, AWS	|	57.0 MB	|	p16_e41_PCAII_tumorintrinsic
MEL53	|	unmicst-LSP11635_cell.csv	|	HTAN, AWS	|	42.5 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL54	|	LSP11642--unmicst_cellRing.csv	|	HTAN, AWS	|	126.6 MB	|	p16_e41_PCAII_tumorintrinsic
MEL54	|	unmicst-LSP11643_cell.csv	|	HTAN, AWS	|	128.7 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL55	|	LSP11658--unmicst_cellRing.csv	|	HTAN, AWS	|	149.5 MB	|	p16_e41_PCAII_tumorintrinsic
MEL55	|	unmicst-LSP11659_cell.csv	|	HTAN, AWS	|	106.6 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL56	|	unmicst-LSP11667_cell.csv	|	HTAN, AWS	|	29.1 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL58	|	LSP11690--unmicst_cellRing.csv	|	HTAN, AWS	|	226.3 MB	|	p16_e41_PCAII_tumorintrinsic
MEL58	|	unmicst-LSP11691_cell.csv	|	HTAN, AWS	|	259.8 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL59	|	LSP11698--unmicst_cellRing.csv	|	HTAN, AWS	|	86.7 MB	|	p16_e41_PCAII_tumorintrinsic
MEL60	|	LSP11706--unmicst_cellRing.csv	|	HTAN, AWS	|	32.8 MB	|	p16_e41_PCAII_tumorintrinsic
MEL60	|	unmicst-LSP11707_cell.csv	|	HTAN, AWS	|	9.4 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL61	|	LSP11714--unmicst_cellRing.csv	|	HTAN, AWS	|	77.0 MB	|	p16_e41_PCAII_tumorintrinsic
MEL62	|	LSP11720--unmicst_cellRing.csv	|	HTAN, AWS	|	10.4 MB	|	p16_e41_PCAII_tumorintrinsic
MEL64	|	LSP11738--unmicst_cellRing.csv	|	HTAN, AWS	|	41.6 MB	|	p16_e41_PCAII_tumorintrinsic
MEL64	|	unmicst-LSP11739_cell.csv	|	HTAN, AWS	|	32.8 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL65	|	LSP11746--unmicst_cellRing.csv	|	HTAN, AWS	|	46.7 MB	|	p16_e41_PCAII_tumorintrinsic
MEL65	|	unmicst-LSP11747_cell.csv	|	HTAN, AWS	|	60.7 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL66	|	LSP11754--unmicst_cellRing.csv	|	HTAN, AWS	|	13.3 MB	|	p16_e41_PCAII_tumorintrinsic
MEL67	|	LSP11762--unmicst_cellRing.csv	|	HTAN, AWS	|	31.3 MB	|	p16_e41_PCAII_tumorintrinsic
MEL68	|	LSP11770--unmicst_cellRing.csv	|	HTAN, AWS	|	39.7 MB	|	p16_e41_PCAII_tumorintrinsic
MEL68	|	unmicst-LSP11771_cell.csv	|	HTAN, AWS	|	30.8 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL68	|	LSP11778--unmicst_cellRing.csv	|	HTAN, AWS	|	57.0 MB	|	p16_e41_PCAII_tumorintrinsic
MEL69	|	LSP11786--unmicst_cellRing.csv	|	HTAN, AWS	|	73.9 MB	|	p16_e41_PCAII_tumorintrinsic
MEL50	|	unmicst-LSP12422_cell.csv	|	HTAN, AWS	|	39.7 MB	|	RP-p16-e24_PCAphaseII_lineage
MEL50	|	LSP12424--unmicst_cellRing.csv	|	HTAN, AWS	|	45.9 MB	|	p16_e41_PCAII_tumorintrinsic
MEL70	|	LSP13078--unmicst_cellRing.csv	|	HTAN, AWS	|	1.548 GB	|	p135_e9_PCAlineage
MEL73	|	LSP13102--unmicst_cellRing.csv	|	HTAN, AWS	|	547.9 MB	|	p135_e9_PCAlineage
MEL71	|	LSP13179--unmicst_cellRing.csv	|	HTAN, AWS	|	922.0 MB	|	p135_e9_PCAlineage
MEL72	|	LSP13186--unmicst_cellRing.csv	|	HTAN, AWS	|	998.0 MB	|	p135_e9_PCAlineage
MEL74	|	LSP15120--unmicst_cellRing.csv	|	HTAN, AWS	|	730.9 MB	|	p135_e9_PCAlineage
MEL75	|	LSP15129--unmicst_cellRing.csv	|	HTAN, AWS	|	1.47 GB	|	p135_e9_PCAlineage
MEL76	|	LSP15138--unmicst_cellRing.csv	|	HTAN, AWS	|	166.7 MB	|	p135_e9_PCAlineage
MEL78	|	LSP15156--unmicst_cellRing.csv	|	HTAN, AWS	|	734.8 MB	|	p135_e9_PCAlineage
MEL79	|	LSP15165--unmicst_cellRing.csv	|	HTAN, AWS	|	92.5 MB	|	p135_e9_PCAlineage
MEL80	|	LSP15174--unmicst_cellRing.csv	|	HTAN, AWS	|	558.2 MB	|	p135_e9_PCAlineage
MEL81	|	LSP15183--unmicst_cellRing.csv	|	HTAN, AWS	|	218.7 MB	|	p135_e9_PCAlineage
MEL82	|	LSP15192--unmicst_cellRing.csv	|	HTAN, AWS	|	1.682 GB	|	p135_e9_PCAlineage
MEL83	|	LSP15201--unmicst_cellRing.csv	|	HTAN, AWS	|	125.8 MB	|	p135_e9_PCAlineage
MEL84	|	LSP15210--unmicst_cellRing.csv	|	HTAN, AWS	|	371.7 MB	|	p135_e9_PCAlineage
MEL85/MEL86	|	LSP15219--unmicst_cellRing.csv	|	HTAN, AWS	|	310.1 MB	|	p135_e9_PCAlineage

​
​  
  
  
--------------------------
ADDITIONAL NOTES/COMMENTS
--------------------------
​
Please contact tissue-atlas(at)hms.harvard.edu if you have any questions related to the data.
