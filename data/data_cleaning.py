'''Data was released Mar 29. Before summer uptick.
SQL query below to extract and format data correctly
SELECT DISTINCT l.zip, l.county, p.person_id, p.gender_source_value, p.birth_datetime, p.death_datetime, p.race_source_value, p.ethnicity_source_value, c.condition_start_datetime, c.condition_concept_id
FROM person p
INNER JOIN condition_occurrence c ON c.person_id = p.person_id
INNER JOIN location l on l.location_id = p.location_id
WHERE condition_concept_id = '37311061' --Disease caused by 2019-nCoV


***********
Must do all pep8 documentation still
***********
'''

import pandas as pd
import os
from os import path
import os.path
import pathlib

def read_patient_data(patient_data):
    '''
    Reads in the data for patient-level data.

    Args:
        patient_data (str): the path to the patient-level data. Should be formatted like:
        *********************
        *********************

    Returns:
        pandas dataframe of the csv file read into it
    '''
    file_to_read = patient_data
    if os.path.exists(file_to_read): #tests whether or not this csv file exists
        csv_as_df = pd.read_csv(file_to_read, encoding = 'utf-8')
    else:
        raise NameError(f'{file_to_read} does not exist')
    return csv_as_df

def read_pop_data(population_data):
    '''
    Reads in the data for population data (census data).

    Args:
        population_data (str): the path to the census data. 
        data contains positive cases, gender, race/ethnicity, death, birth.
        Should be formatted like:
        *********************
        *********************

    Returns:
        pandas dataframe of the csv file read into it
    '''
    file_to_read = population_data
    if os.path.exists(file_to_read): #tests whether or not this csv file exists
        csv_as_df = pd.read_csv(file_to_read, encoding = 'utf-8')
    else:
        raise NameError(f'{file_to_read} does not exist') #if file to read doesn't exist, raise error!
    return csv_as_df

def county_cleaning(patient_dataset):
    '''
    improve documentation
    '''
    if 'county' not in patient_dataset:
        raise NameError('No column named "county"')
    if 'condition_start_datetime' not in patient_dataset:
        raise NameError('No column named "condition_start_datetime"')
    if 'death_datetime' not in patient_dataset:
        raise NameError('No column named "death_datetime"')
    data = patient_dataset
    #remove the word 'county' from the county column
    data['county'] = data['county'].str.split(' ').str[0]
    data['condition_month'] = pd.DatetimeIndex(data['condition_start_datetime']).month
    death = data [data['death_datetime'].notna()]
    return data,death

#cases by county
#some persons have multiple entries (unique cases)
def features_by_county(patient_data, death_data):
    '''
    improve documentation
    '''
    data = patient_data
    death = death_data
    data_pos = data.groupby(['county',
                            'condition_month',
                            'gender_source_value',
                            'race_source_value', 
                            'ethnicity_source_value']).size().reset_index(name='positive_counts')
    data_death = death.groupby(['county', 
                                'condition_month',
                                'gender_source_value',
                                'race_source_value', 
                                'ethnicity_source_value']).size().reset_index(name='death_counts')
    return data_pos,data_death

    
def merge_data(data_pos, data_death, pop):
    '''
    add documentation
    '''
    data_flat = pd.merge(data_pos, data_death, on = ['county', 
                                                        'condition_month', 
                                                        'gender_source_value', 
                                                        'race_source_value',
                                                        'ethnicity_source_value'], how="outer")
    data_flat_pop_fips = pd.merge(data_flat, pop, on = ['county'])
    data_flat_pop_fips.fillna(value=0, inplace=True) #filling in the NaN with 0
    return data_flat_pop_fips


def write_file_for_viz(data_flat_pop_fips, path):
    nan_columns = []
    for column in data_flat_pop_fips.columns:
        if False in data_flat_pop_fips[column].isna().tolist():
            nan_columns.append(column)
    if nan_columns != []:
        raise ValueError('Nan values in ' + str([column for column in nan_columns]))
    data_flat_pop_fips.to_csv(path, sep = ',')