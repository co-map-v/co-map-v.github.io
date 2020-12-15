"""
Unit tests for data cleaning. Pylint = 10.00
"""
import unittest
import os
import pathlib
import numpy as np
import pandas as pd
from comapv.data import data_cleaning


class UnitTests(unittest.TestCase):
    """
    Unit test class
    """
    def test_column_names_for_covid_data(self):
        """
        This function tests whether the input pandas dataframe for county_cleaning
        has the correct names for columns or not in data_cleaning.py

        Args:
            Self

        Returns:
            Ok if the column names are all correctly named.

            Error message 'No column named [list of incorrect column names]' if there are
            incorrect column names in pandas dataframe.
        """
        table = pd.DataFrame({'county1': ['County1','County2'],'condition': [1,2],
                            'deaths': [1,2]})
        with self.assertRaises(NameError):
            data_cleaning.county_cleaning(table)

    def test_column_names_for_pop_data(self):
        """
        This function tests whether the input pandas dataframe for merge_data
        has the correct names for columns or not in data_cleaning.py

        Args:
            Self

        Returns:
            Ok if the column names are all correctly named.

            Error message 'No column named [list of incorrect column names]' if there are
            incorrect column names in pandas dataframe.
        """
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
        """
        This function tests whether the input pandas dataframe for county_cleaning
        has the correct data types (dtypes) for columns or not in data_cleaning.py

        Args:
            Self

        Returns:
            Ok if the column dtypes are all correct.

            Error message 'The following columns have incorrect dtypes: 
            [list of columns with incorrect dtypes]' if there are incorrect dtypes 
            in columns in pandas dataframe.
        """
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
        """
        This function tests whether the input pandas dataframe for merge_data
        has the correct data types (dtypes) for columns or not in data_cleaning.py

        Args:
            Self

        Returns:
            Ok if the column dtypes are all correct.

            Error message 'The following columns have incorrect dtypes: 
            [list of columns with incorrect dtypes]' if there are incorrect dtypes 
            in columns in pandas dataframe.
        """
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
        """
        This function tests whether the input pandas dataframe for write_file_for_viz
        has NaN values in columns or not in data_cleaning.py

        Args:
            Self

        Returns:
            Ok if there are no NaN values.

            Error message 'Nan values in [list of columns with NaN values]' if there are NaN 
            in columns in pandas dataframe.
        """
        table = pd.DataFrame({'county1': [np.nan,'County2'],'condition': [1,2],
                            'deaths': [1,2]})
        path = ' '
        with self.assertRaises(ValueError):
            data_cleaning.write_file_for_viz(table,path)

    def test_county_names(self):
        """
        This function tests whether the input pandas dataframe for county_cleaning
        has the same county names in county column as GeoJSON file's county names.

        Args:
            Self

        Returns:
            Ok if the county names in county coliumn are the same as those of GeoJSON file.

            Error message 'County name in column is different from GeoJSON county name' 
            if there are county names that are different from those of GeoJSON file.
        """
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
        """
        This function tests for whether or not the output of
        read_patient_data(patient_data_path) from
        data_cleaning.py is a pandas dataframe.

        Args:
            Self

        Returns:
            Ok if the output of of read_patient_data(patient_data_path) from
            data_cleaning.py is a pandas dataframe.

            Error message 'data output is not in dataframe format' if output of of
            read_patient_data(patient_data_path) from data_cleaning.py is not a pandas dataframe.

        """
        # get wd of this script being run
        wd_of_script = pathlib.Path(__file__).parent.absolute()
        patient_data_path = os.path.join(wd_of_script, '../data', 'data-1605136079581.csv') #filepath to the data
        dataframe = data_cleaning.read_patient_data(patient_data_path)
        self.assertTrue(isinstance(dataframe, pd.DataFrame),
                        'data output is not in dataframe format')

    def test_read_pop_data_output_type(self):
        """
        This function tests for whether or not the output of read_pop_data(patient_data_path) from
        data_cleaning.py is a pandas dataframe.

        Args:
            Self

        Returns:
            Ok if the output of of read_pop_data(patient_data_path) from
            data_cleaning.py is a pandas dataframe.

            Error message 'data output is not in dataframe format' if output of of
            read_pop_data(patient_data_path) from data_cleaning.py is not a pandas dataframe.

        """
        # get wd of this script being run
        wd_of_script = pathlib.Path(__file__).parent.absolute()
        patient_data_path = os.path.join(wd_of_script, '../data', 'population2010.csv') #filepath to the data
        dataframe = data_cleaning.read_pop_data(patient_data_path)
        self.assertTrue(isinstance(dataframe, pd.DataFrame),
                        'data output is not in dataframe format')

    def test_feature_counts_greater_than_pop(self):
        """
        This function tests for whether or not the final output file of data_cleaning.py
        has features (Deaths or Cases) that exceed the population.

        Args:
            Self

        Returns:
            Ok if deaths or cases do not exceed the population
            Error message if if deaths or cases do exceed the population

        """
        features_within_range = True # set default
        # get wd of this script being run
        wd_of_script = pathlib.Path(__file__).parent.absolute()
        #ensure this is the name of your output file fed into viz
        filepath_read = os.path.join(wd_of_script, '../data', 'covid_ma_positive_death_counts.csv') # filepath to the data

        #read in the final output file of data_cleaning.py
        dataframe = pd.read_csv(filepath_read)
        #new column for deaths/pop
        dataframe['death_pop_ratio'] = dataframe['death_counts']/dataframe['population_2010']
        #new column for cases/pop
        dataframe['cases_pop_ratio'] = dataframe['positive_counts']/dataframe['population_2010']

        max_death_pop_ratio = dataframe['death_pop_ratio'].max() #get max ration deaths/pop
        max_cases_pop_ratio = dataframe['cases_pop_ratio'].max() #get max ratio cases/pop
        if max_death_pop_ratio > 1 or max_cases_pop_ratio > 1:
            features_within_range = False
        message = 'feature counts (deaths or cases) exceed population' #message for failure
        self.assertTrue(features_within_range, message) #test if features are within range or not

    def test_write_file_for_viz(self):
        """
        This function tests for whether or not function
        write_file_for_viz(dataframe, filename_to_write)
        from data_cleaning.py creates a file in the location and named as it is instructed
        to do. This test creates a file named 'test_cleaned_dataset.csv' using write_file_for_viz,
        checks whether it exists or not, then deletes that file after the test.

        Args:
            Self

        Returns:
            Ok if the file (named properly and in the correct location) exists
            Error message if if deaths or cases do exceed the population

        """
        # get wd of this script being run
        wd_of_script = pathlib.Path(__file__).parent.absolute()
        filepath_read = os.path.join(wd_of_script, '../data', 'covid_ma_positive_death_counts.csv') # filepath to the data
        dataframe = pd.read_csv(filepath_read)
        filename_to_write = 'test_cleaned_dataset.csv' # dummy output to then be deleted later
        data_cleaning.write_file_for_viz(dataframe, filename_to_write) # writes the csv file
        message = 'file does not exist'
        self.assertTrue(os.path.exists(filename_to_write), message) # does the csv we write exist?
        if os.path.exists(filename_to_write): # tests whether or not this csv file exists
            os.remove(filename_to_write) # removes the file if it exists
        else:
            pass

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)
