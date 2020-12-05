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
    csv_as_df = pd.read_csv(patient_data, encoding = 'utf-8')
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
    csv_as_df = pd.read_csv(population_data, encoding = 'utf-8')
    return csv_as_df

def county_cleaning(patient_dataset):
    '''
    improve documentation
    '''
    data = patient_dataset
    #remove the word 'county' from the county column
    data['county'] = data['county'].str.split(' ').str[0]
    data['condition_month'] = pd.DatetimeIndex(data['condition_start_datetime']).month
    death = data [data['death_datetime'].notna()]
    result = (data, death)
    return result



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
    result = (data_pos, data_death)
    return result

    
def merge_data(data_pos, data_death, pop):
    '''
    add documentation
    '''

    data_flat = pd.merge (data_pos, data_death, on = ['county', 
                                                        'condition_month', 
                                                        'gender_source_value', 
                                                        'race_source_value',
                                                        'ethnicity_source_value'], how="outer")
    data_flat_pop_fips = pd.merge (data_flat, pop, on = ['county'])
    return data_flat_pop_fips


def write_file_for_viz(data_flat_pop_fips, path):
    data_flat_pop_fips.to_csv(path, sep = ',')


