import unittest
import os
import numpy as np
from data import data_cleaning
import pandas as pd
import pathlib


class UnitTests(unittest.TestCase):
    '''
    Unit test class
    '''
    def test_column_names_for_covid_data(self):
        '''
        Test whether column names are correct for COVID data
        '''
        table = pd.DataFrame({'county1': ['County1','County2'],'condition': [1,2],
                            'deaths': [1,2]})
        with self.assertRaises(NameError):
            data_cleaning.county_cleaning(table)

    def test_column_names_for_pop_data(self):
        '''
        Test whether column names are correct for population data
        '''
        pop_table = pd.DataFrame({'county1': ['County1','County2'],'condition': [1,2],
                            'deaths': [1,2]})
        table1 = pd.DataFrame({'zip': [1,2],'county': [1,2],
                            'person_id': [1,2],'gender_source_value': [1,2],
                            'birth_datetime': [1,2], 'death_datetime': [1,2],
                            'race_source_value': [1,2],
                            'ethnicity_source_value': [1,2],
                            'condition_start_datetime': [1,2],
                            'condition_concept_id': [1,2]})
        table2 = pd.DataFrame({'zip': [1,2],'county': [1,2],
                            'person_id': [1,2],'gender_source_value': [1,2],
                            'birth_datetime': [1,2], 'death_datetime': [1,2],
                            'race_source_value': [1,2],
                            'ethnicity_source_value': [1,2],
                            'condition_start_datetime': [1,2],
                            'condition_concept_id': [1,2]})
        with self.assertRaises(NameError):
            data_cleaning.merge_data(table1,table2,pop_table)

    def test_column_type_in_county_cleaning(self):
        '''
        Test whether columns' types are correct for COVID data
        '''
        table = pd.DataFrame({'zip': [1,2],'county': [1,2],
                            'person_id': [1,2],'gender_source_value': [1,2],
                            'birth_datetime': [1,2], 'death_datetime': [1,2],
                            'race_source_value': [1,2],
                            'ethnicity_source_value': [1,2],
                            'condition_start_datetime': [1,2],
                            'condition_concept_id': [1,2]})
        with self.assertRaises(ValueError):
            data_cleaning.county_cleaning(table)

    def test_column_type_in_merge_data(self):
        '''
        Test whether columns' types are correct for population data
        '''
        pop_table = pd.DataFrame({'fips_code':[1.5,1.6],'county':['King','King'],
                                'population_2010':[1,0]})
        table1 = pd.DataFrame({'zip': [1,2],'county': [1,2],
                            'person_id': [1,2],'gender_source_value': [1,2],
                            'birth_datetime': [1,2], 'death_datetime': [1,2],
                            'race_source_value': [1,2],
                            'ethnicity_source_value': [1,2],
                            'condition_start_datetime': [1,2],
                            'condition_concept_id': [1,2]})
        table2 = pd.DataFrame({'zip': [1,2],'county': [1,2],
                            'person_id': [1,2],'gender_source_value': [1,2],
                            'birth_datetime': [1,2], 'death_datetime': [1,2],
                            'race_source_value': [1,2],
                            'ethnicity_source_value': [1,2],
                            'condition_start_datetime': [1,2],
                            'condition_concept_id': [1,2]})
        with self.assertRaises(ValueError):
            data_cleaning.merge_data(table1,table2,pop_table)

    def test_nan(self):
        '''
        Test there are nan values in columns
        '''
        table = pd.DataFrame({'county1': [np.nan,'County2'],'condition': [1,2],
                            'deaths': [1,2]})
        path = ' '
        with self.assertRaises(ValueError):
            data_cleaning.write_file_for_viz(table,path)

    def test_county_names(self):
        '''
        Test whether county names are correctly named
        '''
        table = pd.DataFrame({'zip': [1,2],'county': ['KingCounty','King'],
                            'person_id': [1,2],'gender_source_value': [1,2],
                            'birth_datetime': [1,2], 'death_datetime': [1,2],
                            'race_source_value': [1,2],
                            'ethnicity_source_value': [1,2],
                            'condition_start_datetime': [1,2],
                            'condition_concept_id': [1,2]})
        with self.assertRaises(ValueError):
            data_cleaning.county_cleaning(table)

    def test_read_patient_data_output_type(self):
        # CHANGE THIS TO BE THE TEST FOR THE TYPE OF WHAT WE WANT (PANDAS DF)
        # get wd of this script being run where the data are
        wd_of_script = pathlib.Path(__file__).parent.absolute()
        patient_data_path = os.path.join(wd_of_script, 'data', 'data-1605136079581.csv')
        dataframe = data_cleaning.read_patient_data(patient_data_path)
        self.assertTrue(isinstance(dataframe, pd.DataFrame),
                        'data output is not in dataframe format')

    def test_read_pop_data_output_type(self):
        # get wd of this script being run where the data are
        wd_of_script = pathlib.Path(__file__).parent.absolute()
        patient_data_path = os.path.join(wd_of_script, 'data', 'population2010.csv')
        dataframe = data_cleaning.read_pop_data(patient_data_path)
        self.assertTrue(isinstance(dataframe, pd.DataFrame),
                        'data output is not in dataframe format')

    def feature_counts_greater_than_pop(self):
        features_within_range = 'True' # set default
        # get wd of this script being run where the data are
        wd_of_script = pathlib.Path(__file__).parent.absolute()
        #ensure this is the name of your output file fed into viz
        filepath_read = os.path.join(wd_of_script, 'data', 'covid_ma_positive_death_counts.csv')
        dataframe = pd.read_csv(filepath_read)
        dataframe['death_pop_ratio'] = dataframe['death_counts']/dataframe['population_2010']
        dataframe['cases_pop_ratio'] = dataframe['positive_counts']/dataframe['population_2010']
        max_death_pop_ratio = dataframe['death_pop_ratio'].max()
        max_cases_pop_ratio = dataframe['cases_pop_ratio'].max()
        if max_death_pop_ratio > 1 | max_cases_pop_ratio > 1:
            features_within_range = 'False'
        self.assertTrue(features_within_range, 'True')
        #, 'feature counts (deaths or cases) exceed population')

    def test_write_file_for_viz(self): # must adjust to be the data_fips data but as a toy dataset
        # get wd of this script being run where the data are
        wd_of_script = pathlib.Path(__file__).parent.absolute()
        filepath_read = os.path.join(wd_of_script, 'data', 'covid_ma_positive_death_counts.csv')
        dataframe = pd.read_csv(filepath_read)
        filename_to_write = 'test_cleaned_dataset.csv' # dummy output to then be deleted later
        data_cleaning.write_file_for_viz(dataframe, filename_to_write) # writes the csv file
        self.assertTrue(os.path.exists(filename_to_write)) # does the csv we write exist?
        if os.path.exists(filename_to_write): # tests whether or not this csv file exists
            os.remove(filename_to_write) # removes the file if it exists
        else:
            pass

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)
