#!/usr/bin/env python3


'''
Alan - this code imports functions from data_cleaning.py. We need to add some
if statement rules within data_cleaning.py (e.g. if statements to then raiseValueError), 
then import the functions from data_cleaning into our unittests to test. Leave this script 
alone because this is the clean script we want to run for our data cleaning pipeline.
'''

from data_cleaning import read_patient_data
from data_cleaning import read_pop_data
from data_cleaning import county_cleaning
from data_cleaning import features_by_county
from data_cleaning import merge_data
from data_cleaning import write_file_for_viz
import os
import pathlib
import pandas as pd

#read in the data

WD_OF_SCRIPT = pathlib.Path(__file__).parent.absolute() # get wd of this script being run where the data are
PATIENT_DATA_PATH = os.path.join(WD_OF_SCRIPT, 'data-1605136079581.csv')
POPULATION_DATA_PATH = os.path.join(WD_OF_SCRIPT, 'population2010.csv')
DATA = read_patient_data(patient_data_path)
POP = read_pop_data(population_data_path)

#clean the data
DATA,DEATH = county_cleaning(data)
# death = county_cleaning(data)[1]

#generate features
DATA_POS, DATA_DEATH = features_by_county(data, death)
# data_death = features_by_county(death, death)[1]

#create dataframe for visualization
DATA_FLAT_POP_FIPS = merge_data(data_pos, data_death, pop)

#write dataframe to csv file in data
OUTPUT_DIRECTORY = os.path.join(WD_OF_SCRIPT, 'covid_ma_positive_death_counts.csv')
write_file_for_viz(DATA_FLAT_POP_FIPS, OUTPUT_DIRECTORY)