# RoadSafety
---

## Summary
This final project for COSC445 attempts to analyze highway accidents across the United States from the years 2010, 2014, and 2018. We found that in some cases higher speed limits did indicate to some states being higher on the list for either cumulative or normalized accidents. Although, it should be noted that this correlation is fairly weak and can change with different years. For future work, we would like to incorporate more FARS data from years past 2010 as well as other features from other datasets, such as the highway integrity and highway network length.

## Results
To see the results of this project, please open the interactive python notebook (ipynb) named [multiyear_analysis.ipynb](https://github.com/fdac20/RoadSafety/blob/master/multiyear_analysis.ipynb).

To see a deeper analysis and other details of the project, please reference the [final report document](https://github.com/fdac20/RoadSafety/blob/master/CS445_Final_Report.pdf)

## Requirements

### Prerequisites:

**Important Note:**
The easiest way of setting up an environment to run this notebook would be to use **Anaconda**. If you have Anaconda installed, then in the root directory, simply running `conda env create -f environment.yaml` will create a virtual environment called `road`. You can activate the environment by running `conda activate road`, and then you can launch Jupyter to access the main notebook `multiyear_analysis.ipynb`.

- python 3.5+
- matplotlib
- cartopy
- numpy
- seaborn
- tqdm
- geojson
- pandas
- jupyter notebook

### Dataset Setup
- Download FARS CSV datasets from 2010, 2014, and 2018 from this repository: https://www.nhtsa.gov/node/97996/251
	- Only download the zip file in the "National" subfolder of each year
	- Extract the contents into their own folder following the naming format: FARS[YEAR]NationalCSV (ex: if 2010 is chosen, then the folder that the contents that would have been extracted to would be named FARS2010NationalCSV)
- Download US shape data from this link: https://biogeo.ucdavis.edu/data/gadm3.6/shp/gadm36_USA_shp.zip and extract all of its contents into this git folder under the folder name "shapes".
