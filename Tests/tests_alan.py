import sys
sys.path.append("../data")
import unittest
import data_cleaning
import pandas as pd
import numpy as np


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

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)