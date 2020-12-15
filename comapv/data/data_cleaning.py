'''Data was released Mar 29. Before summer uptick.
SQL query below to extract and format data correctly
SELECT DISTINCT l.zip, l.county, p.person_id, p.gender_source_value,
p.birth_datetime, p.death_datetime, p.race_source_value,
p.ethnicity_source_value, c.condition_start_datetime,
c.condition_concept_id
FROM person p
INNER JOIN condition_occurrence c ON c.person_id = p.person_id
INNER JOIN location l on l.location_id = p.location_id
WHERE condition_concept_id = '37311061' --Disease caused by 2019-nCoV
***********
Must do all pep8 documentation still
***********

Pylint = 9.57
'''

import json
import os
import urllib.request
import numpy as np
import pandas as pd

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
        raise NameError(f'{file_to_read} does not exist')
        # if file to read doesn't exist, raise error!
    return csv_as_df

def county_cleaning(patient_dataset):
    '''
    Clean up patient_dataset's county, condition_start_datetime, and death_datetime
    columns.

    Args:
        patient_dataset (dataframe): pandas dataframe

    Returns:
        Two pandas dataframes
    '''
    columns = ['zip','county','person_id','gender_source_value','birth_datetime',
                'death_datetime','race_source_value','ethnicity_source_value',
                'condition_start_datetime','condition_concept_id']
    incorrect_columns = []
    county_names = []
    incorrect_dtypes = []

    for column in columns:
        if column not in patient_dataset:
            incorrect_columns.append(column)
    if incorrect_columns != []:
        raise NameError('No column named ' + str(incorrect_columns))

    for column in patient_dataset.columns:
        if column == 'zip':
            if patient_dataset[column].dtype != 'float64':
                incorrect_dtypes.append(column)
        elif column == 'person_id' or column == 'condition_concept_id':
            if patient_dataset[column].dtype != 'int64':
                incorrect_dtypes.append(column)
        else:
            if patient_dataset[column].dtype != 'object':
                incorrect_dtypes.append(column)
    if incorrect_dtypes != []:
        raise ValueError('The following columns have incorrect dtypes: ',
                            incorrect_dtypes)

    data = patient_dataset
    #remove the word 'county' from the county column
    data['county'] = data['county'].str.split(' ').str[0]

    with urllib.request.urlopen(
        'https://raw.githubusercontent.com/co-map-v/co-map-v.github.io/main/data/ma_map.geojson')\
        as response:
        counties = json.load(response)

    for i in range(len(counties['features'])):
        county_names.append(counties['features'][i]['properties']['NAME'])

    nparray = np.array(county_names)
    df_county = pd.unique(data['county'])
    same = []

    for i in range(nparray.shape[0]):
        for j in range(df_county.shape[0]):
            if nparray[i] == df_county[j]:
                same.append(nparray[i])
    if same == []:
        raise ValueError('County name in column is different from GeoJSON county name')\

    data['condition_month'] = data['condition_start_datetime'].dt.month
    death = data [data['death_datetime'].notna()]
    return data,death

#cases by county
#some persons have multiple entries (unique cases)
def features_by_county(patient_data, death_data):
    '''
    Groups cases by county

    Args:
        patient_data (dataframe): pandas dataframe
        death_data (dataframe): pandas dataframe

    Returns:
        Two pandas dataframes
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
    Merge data_pos, data_death, and pop together as one dataframe

    Args:
        dadta_pos (dataframe): pandas dataframe
        data_death (dataframe): pandas dataframe

    Returns:
        One pandas dataframe
    '''
    incorrect_dtypes = []
    columns = ['fips_code','county','population_2010']
    incorrect_columns = []

    for column in columns:
        if column not in pop:
            incorrect_columns.append(column)
        else:
            pass
    if incorrect_columns != []:
        raise NameError('No column named ' + str(incorrect_columns))

    for column in pop.columns:
        if column == 'fips_code' or column == 'population_2010':
            if pop[column].dtype != 'int64':
                incorrect_dtypes.append(column)
        else:
            if pop[column].dtype != 'object':
                incorrect_dtypes.append(column)
    if incorrect_dtypes != []:
        raise ValueError('The following columns have incorrect dtypes: ',
                            incorrect_dtypes)

    data_flat = data_pos.merge (data_death, how='outer')
    data_flat_pop_fips = data_flat.merge (pop, how='outer')

    data_flat_pop_fips.fillna(value=0, inplace=True) #filling in the NaN with 0
    return data_flat_pop_fips

def write_file_for_viz(data_flat_pop_fips, path):
    '''
    Writes out pandas dataframe into csv file for visualization

    Args:
        data_flat_pop_fips (dataframe): pandas dataframe
        path (string): save path for csv file

    Returns:
        None
    '''
    nan_columns = []
    for column in data_flat_pop_fips.columns:
        if True in data_flat_pop_fips[column].isna().tolist():
            nan_columns.append(column)
    if nan_columns != []:
        raise ValueError('Nan values in ' + str([column for column in nan_columns]))

    data_flat_pop_fips.to_csv(path, sep=',')
