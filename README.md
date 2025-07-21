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
​
​
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
<List all files (or folders, as appropriate for dataset organization) contained in each repository, with a brief description. If you are depositing certain file types into public, standardized repositories that already include a file index & metadata, you can link to that repository instead of listing all individual files. For all other data, (on AWS, etc) list all files. >  
​
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
|ID | ID.ome.tif | AWS     | N.N KB |

​

### Feature Table Data
|Patient ID | File Name      | Location | File size | CyCIF Panel |
|------- | ------------|------------|-----------|-------|
|ID | ID.csv |  |  |
​
​  
  
  
--------------------------
ADDITIONAL NOTES/COMMENTS
--------------------------
​
Please contact tissue-atlas(at)hms.harvard.edu if you have any questions related to the data.
