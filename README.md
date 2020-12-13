[![Build Status](https://travis-ci.org/co-map-v/co-map-v.github.io.svg?branch=main)](https://travis-ci.org/co-map-v/co-map-v.github.io)
[![Coverage Status](https://coveralls.io/repos/github/co-map-v/co-map-v.github.io/badge.svg?branch=main)](https://coveralls.io/github/co-map-v/co-map-v.github.io?branch=main)

<img src="https://raw.githubusercontent.com/co-map-v/co-map-v.github.io/main/docs/website/img/logo.png" width=15% height=15%>



# CO-MAP-V: COVID-19 Massachusetts Map + Visualization Tool

CO-MAP-V is a Python-based dynamic visualization tool built on [Plotly] and [Dash], and implemented through [Heroku]. It generates an easy-to-use comparative clickable interface depicting county-level Synthea data in the OMOP common data model to vizualize an outbreak of COVID-19 in Massachusetts for the time period January-March 2020. It provides simple options for time-series comparisons with month-specific interactive timesliders. 
###### Access CO-MAP-V at: [co-map-v.github.io](https://co-map-v.github.io)


##### Included in the dashboard:
- Maps and complementary histograms of month-specific data pertaining to:
    -  Number of deaths per county; 
    -  Number of positive case counts per county; 
    -  Population density per county (based on 2010 US Census estimates).

#### Background
Current COVID-19 research focuses on increasing our understanding of how the virus spreads through communities and neighborhoods. Given the novelty of the virus, researchers face many challenges and unknowns. First, obtaining access to patient data can be a limiting factor, especially as patient data is protected and governed by the Health Insurance Portability and Accountability Act (HIPAA). Second, understanding the trends of the data may be difficult as data representation and visualization methods are highly variable, making the data subject to interpretability. Synthetic data -- simulated data that are generated based on the trends and patterns of real data -- may provide an avenue for researchers to better understand real-world data trends without the need to overcome the obstacles involved in obtaining real patient data. Since synthetic data may be modeled on real-world data, it may allow researchers to generate results that are meaningful and translatable while being more accessible.

#### Goals:
- With the synthetic COVID-19 data, we aim to build a visualization dashboard that features a choropleth map as well as a complementary chart.
- With the dashboard, we aim to allow users (both those experienced and inexperienced with public health methods) to explore the trends and geographic spread of COVID-19 in Massachusetts.
- Seek to create an open exploratory visualization tool framework that allows users who have basic Python, GeoJSON and data cleaning knowledge to make visualizations from their own COVID-19 demographic data in the Observational Medical Outcomes Partnership (OMOP) common data format, and include an appropriate GeoJSON, with minimal effort. 

#### Directory Structure
```
co-map-v.github.io/
  |- data/
     |- Old/
        |- ... (Contains various files that are no longer used)
     |- data_backup/ 
        |- ... (Contains backup files)
     |- __init__.py
     |- covid_ma_positive_death_counts.csv (output of data_clean.py and input of app.py)
     |- data-1605136079581.csv (input of data_clean.py)
     |- data_clean.py
     |- data_cleaning.py
     |- ma_map_geojson
     |- population2010.csv
  |- docs/
     |- website/
        |- ... (Contains JS, CSS, images for website)
     |- Component Specification.pdf
     |- Functional Specification.pdf
     |- Technology review presentation.pdf
     |- Final presentation.pdf
     |- index.html (GitHub Pages)
  |- tests/
     |- .coverage
     |- __init__.py
     |- tests.py
     |- tests_viz.py
     |- smoketest_data.csv
  |- .coverage (Coverage)
  |- .coveragerc (Coverage)
  |- .gitignore
  |- .travis.yml (Travis CI)
  |- LICENSE
  |- Procfile (Heroku)
  |- README.md
  |- app.py (Heroku)
  |- environment.yml  (Travis CI)
  |- requirements.txt (Heroku)
```

#### Data

Our dataset is a synthetic COVID-19 created by Synthea that was later converted into the OMOP common data model. The data can be found at the [OHDSI] site. 

The data spans a period of three months, January 2020 to March 2020, mimicking the start of the pandemic and contains approximately 10,000 unique patients. The OMOP model is used and thus we have the following data tables at our disposal: `cdm_source`, `condition_era`, `condition_occurrence`, `death`, `drug_era`, `drug_exposure`, `location`, `measurement`, `observation_period`, `observation`, `person`, `procedure_occurrence`, `visit_occurrence`. 

Each of the data tables have their own keys, but can be joined by `person_id`. All of the available data tables are not utilized in this project since many are irrelevant to our use cases. Our analysis will be within the `condition_occurrence`, `death`, `location`, and `person` tables. Within the `person` table, we will be able to obtain the `gender`, `race`, `ethnicity`, and `death date` (if applicable). The `location table` contains the physical address of the patient. Although there is a ZIP code field within the location table, we have estimated that ~50% of the column is not available; therefore, we will be utilizing the `county` field instead. COVID-19 information is stored in the `condition` table. Using the Athena vocabulary standard, we have determined that a `condition_concept_id` of '37311061' indicates ‘Disease caused by 2019-nCoV’ (the virological name of the virus that causes COVID-19). Additionally, we incorporate the latest [United States 2010 Census data] for Massachusetts. 

To fully geographically visualize the data, we use GeoJSON file of Massachusetts representing county boundaries. Ideally, geographic-demographic data table joining is completed based on Federal Information Processing Standard (FIPS) code. However, our synthetic dataset does not include FIPS codes, and so we have opted to perform spatial joins by simple county name (i.e. “Hampshire”, not “Hampshire County”). The particular GeoJSON file we are using is found at the [TopoJSON Github Repository] of topographic GeoJSON files for open use. 

#### More information can be found in the [Functional] and [Component] Specifications (PDF links).

# Technical Information

### Installation and set up

First, make sure that you have Python via Anaconda installed, [https://conda.pydata.org/miniconda.html](https://conda.pydata.org/miniconda.html). 

Use the YML environment file to create an identical environment on your local or remote machine:
    
    conda create --name myenv —environment.yml

For reference: [This is our YML for our conda virtual environment]; and [this is the requirements.txt file].



# Tips for Modifying CO-MAP-V Code for Personal Use

#### Under construction! Check back soon!

         O
       /~~~|#|]|=\|---\__
     |-=_____________  |\\ ,             O       O
    I|_/,-.-.-.-.-,-.\_|='(             T/\     /\=,---.
       ( o )( o )( o )     \            U /\   /\   `O'    cww
        `-'-'-'-'-`-'



[//]: # (Reference Links)

   [Plotly]: <https://www.plotly.com/>
   [Dash]: <https://dash.plotly.com/>
   [OHDSI]: <https://forums.ohdsi.org/t/synthetic-data-with-simulated-covid-outbreak/10256>
   [TopoJSON Github Repository]: <https://www.github.com/deldersveld/topojson/tree/master/countries/us-states>
   [Heroku]: <https://www.heroku.com>
   [Functional]: <https://github.com/co-map-v/co-map-v.github.io/blob/main/docs/Functional%20Specification.pdf>
   [Component]: <https://github.com/co-map-v/co-map-v.github.io/blob/main/docs/Component%20Specification.pdf>
   [This is our YML for our conda virtual environment]: <https://github.com/co-map-v/co-map-v.github.io/blob/main/environment.yml>
   [this is the requirements.txt file]: <https://github.com/co-map-v/co-map-v.github.io/blob/main/requirements.txt>   
