#!/usr/bin/env python3

'''
This is the clean script we want to run for our data cleaning pipeline.
'''

import os
import pathlib
from data import data_cleaning

#read in the data

# get wd of this script being run where the data are
WD_OF_SCRIPT = pathlib.Path(__file__).parent.absolute()

PATIENT_DATA_PATH = os.path.join(WD_OF_SCRIPT, 'data-1605136079581.csv')
POPULATION_DATA_PATH = os.path.join(WD_OF_SCRIPT, 'population2010.csv')
DATA = data_cleaning.read_patient_data(POPULATION_DATA_PATH)
POP = data_cleaning.read_pop_data(POPULATION_DATA_PATH)

#clean the data
DATA,DEATH = data_cleaning.county_cleaning(DATA)
# death = county_cleaning(data)[1]

#generate features
DATA_POS, DATA_DEATH = data_cleaning.features_by_county(DATA, DEATH)
# data_death = features_by_county(death, death)[1]

#create dataframe for visualization
DATA_FLAT_POP_FIPS = data_cleaning.merge_data(DATA_POS, DATA_DEATH, POP)

#write dataframe to csv file in data
OUTPUT_DIRECTORY = os.path.join(WD_OF_SCRIPT, 'covid_ma_positive_death_counts.csv')
data_cleaning.write_file_for_viz(DATA_FLAT_POP_FIPS, OUTPUT_DIRECTORY)
