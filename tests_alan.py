import unittest
from data import data_cleaning
import pandas as pd
import numpy as np
import unittest
import os
from os import path
import os.path
import pathlib


class UnitTests(unittest.TestCase):
    def test_column_names(self):  
        df = pd.DataFrame({'county1': ['County1','County2'],'condition': [1,2],
                            'deaths': [1,2]})      
        with self.assertRaises(NameError):            
            data_cleaning.county_cleaning(df)
    
    def test_nan(self):
        df = pd.DataFrame({'county1': [np.nan,'County2'],'condition': [1,2],
                            'deaths': [1,2]})   
        path = ' '
        with self.assertRaises(ValueError):
            data_cleaning.write_file_for_viz(df,path)

    def test_read_patient_data_output_type(self):  #CHANGE THIS TO BE THE TEST FOR THE TYPE OF WHAT WE WANT (PANDAS DF)
        wd_of_script = pathlib.Path(__file__).parent.absolute() # get wd of this script being run where the data are
        patient_data_path = os.path.join(wd_of_script, 'data', 'data-1605136079581.csv')
        df = data_cleaning.read_patient_data(patient_data_path)
        self.assertTrue(isinstance(df, pd.DataFrame), 'data output is not in dataframe format')

    def test_read_pop_data_output_type(self):
        wd_of_script = pathlib.Path(__file__).parent.absolute() # get wd of this script being run where the data are
        patient_data_path = os.path.join(wd_of_script, 'data', 'population2010.csv')
        df = data_cleaning.read_pop_data(patient_data_path)
        self.assertTrue(isinstance(df, pd.DataFrame), 'data output is not in dataframe format')

    def feature_counts_greater_than_pop(self):
        features_within_range = 'True' #set default
        wd_of_script = pathlib.Path(__file__).parent.absolute() # get wd of this script being run where the data are
        filepath_read = os.path.join(wd_of_script, 'data', 'covid_ma_positive_death_counts.csv') #ensure this is the name of your output file fed into viz
        df = pd.read_csv(filepath_read)
        df['death_pop_ratio'] = df['death_counts']/df['population_2010']
        df['cases_pop_ratio'] = df['positive_counts']/df['population_2010']
        max_death_pop_ratio = df['death_pop_ratio'].max()
        max_cases_pop_ratio = df['cases_pop_ratio'].max()
        if max_death_pop_ratio > 1 | max_cases_pop_ratio > 1:
            features_within_range = 'False'
        self.assertTrue(features_within_range, 'True')#, 'feature counts (deaths or cases) exceed population')

    def test_write_file_for_viz(self): #must adjust to be the data_fips data but as a toy dataset
        wd_of_script = pathlib.Path(__file__).parent.absolute() # get wd of this script being run where the data are
        filepath_read = os.path.join(wd_of_script, 'data', 'covid_ma_positive_death_counts.csv')
        df = pd.read_csv(filepath_read)
        filename_to_write = 'test_cleaned_dataset.csv' #dummy output to then be deleted later
        data_cleaning.write_file_for_viz(df, filename_to_write) #writes the csv file
        self.assertTrue(os.path.exists(filename_to_write)) #does the csv we attempted to write exist?
        if os.path.exists(filename_to_write): #tests whether or not this csv file exists
            os.remove(filename_to_write) #removes the file if it exists
        else:
            pass

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)
