"""
Unit tests to ensure that each function in app.py generates a plotly figure. Pylint = 9.83
"""

import unittest
import os
import json
import urllib.request
import pathlib
import pandas as pd
from ... import app

class UnitTests(unittest.TestCase):

    def test_smoke1 (self):
        """Smoke Test: Death Counts Map

        Should check to see if the function generates a plotly plot
        """
        #URLs left long, ouside of PEP8 compliance to favour readability!
        # Load data from Github Repo
        with urllib.request.urlopen('https://raw.githubusercontent.com/co-map-v/co-map-v.github.io/main/comapv/data/ma_map.geojson') as response:   # pylint: disable=line-too-long
            counties_1 = json.load(response)
        wd_of_script = pathlib.Path(__file__).parent.absolute()
        filepath_read = os.path.join(wd_of_script, './', 'smoketest_data.csv')# pylint: disable=line-too-long
        df_time_1 = pd.read_csv(filepath_read)
        fig = app.death_counts_map(df_time_1,counties_1)
        string = str(type(fig))
        self.assertEqual(string, "<class 'plotly.graph_objs._figure.Figure'>")

    def test_smoke2 (self):
        """Smoke Test: Case Counts Map

        Should check to see if the function generates a plotly plot
        """
        #URLs left long, ouside of PEP8 compliance to favour readability!
        # Load data from Github Repo
        with urllib.request.urlopen('https://raw.githubusercontent.com/co-map-v/co-map-v.github.io/main/comapv/data/ma_map.geojson') as response:   # pylint: disable=line-too-long
            counties_1 = json.load(response)
        wd_of_script = pathlib.Path(__file__).parent.absolute()
        filepath_read = os.path.join(wd_of_script, './', 'smoketest_data.csv')# pylint: disable=line-too-long
        df_time_1 = pd.read_csv(filepath_read)
        fig = app.case_count_map(df_time_1,counties_1)
        string = str(type(fig))
        self.assertEqual(string, "<class 'plotly.graph_objs._figure.Figure'>")

    def test_smoke3 (self):
        """Smoke Test: Pop Counts Map

        Should check to see if the function generates a plotly plot
        """
        #URLs left long, ouside of PEP8 compliance to favour readability!
        # Load data from Github Repo
        with urllib.request.urlopen('https://raw.githubusercontent.com/co-map-v/co-map-v.github.io/main/comapv/data/ma_map.geojson') as response:   # pylint: disable=line-too-long
            counties_1 = json.load(response)
        wd_of_script = pathlib.Path(__file__).parent.absolute()
        filepath_read = os.path.join(wd_of_script, './', 'smoketest_data.csv')# pylint: disable=line-too-long
        df_time_1 = pd.read_csv(filepath_read)
        fig = app.population_map(df_time_1,counties_1)
        string = str(type(fig))
        self.assertEqual(string, "<class 'plotly.graph_objs._figure.Figure'>")

    def test_smoke4 (self):
        """Smoke Test: Pop Counts Chart

        Should check to see if the function generates a plotly plot
        """
        wd_of_script = pathlib.Path(__file__).parent.absolute()
        filepath_read = os.path.join(wd_of_script, './', 'smoketest_data.csv')# pylint: disable=line-too-long
        df_time_1 = pd.read_csv(filepath_read)
        fig = app.population_histogram(df_time_1)
        string = str(type(fig))
        self.assertEqual(string, "<class 'plotly.graph_objs._figure.Figure'>")

    def test_smoke5 (self):
        """Smoke Test: Death Counts Chart

        Should check to see if the function generates a plotly plot
        """
        wd_of_script = pathlib.Path(__file__).parent.absolute()
        filepath_read = os.path.join(wd_of_script, './', 'smoketest_data.csv')# pylint: disable=line-too-long
        df_time_1 = pd.read_csv(filepath_read)
        fig = app.deaths_histogram(df_time_1)
        string = str(type(fig))
        self.assertEqual(string, "<class 'plotly.graph_objs._figure.Figure'>")

    def test_smoke6 (self):
        """Smoke Test: Case Counts Chart

        Should check to see if the function generates a plotly plot
        """
        wd_of_script = pathlib.Path(__file__).parent.absolute()
        filepath_read = os.path.join(wd_of_script, './', 'smoketest_data.csv')# pylint: disable=line-too-long
        df_time_1 = pd.read_csv(filepath_read)
        fig = app.case_histogram(df_time_1)
        string = str(type(fig))
        self.assertEqual(string, "<class 'plotly.graph_objs._figure.Figure'>")

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)
