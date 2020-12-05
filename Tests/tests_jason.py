# CSE 583 Final Project
# Authors: Aja Sutton, Andrew Teng, Jason Thomas, Nanhsuan Yuan
# Autumn 2020

'''
Work in progress. Must adapt the app.py script to have functions to import

'''
import unittest
from data_cleaning import read_patient_data
from data_cleaning import read_pop_data
from data_cleaning import county_cleaning
from data_cleaning import features_by_county
from data_cleaning import merge_data
from data_cleaning import write_file_for_viz
import pandas as pd

# Define a class in which the tests will run
class TestOurDashboard(unittest.TestCase):
        
    def one_shot_test_dataset(self):
        '''
        Tests ____ against test_cleaned_dataset.csv

        Args:
            Self:
        '''
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestOurDashboard)
_ = unittest.TextTestRunner().run(suite)