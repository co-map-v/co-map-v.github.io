import unittest
import os
import json
import pandas as pd
import plotly.express as px
import urllib.request
import pathlib
import sys
sys.path.append('.')
import app

class UnitTests(unittest.TestCase):

    def test_smoke1 (self):
        """Smoke Test: Death Counts Map

        Should check to see if the function generates a plotly plot
        """
        #URLs left long, ouside of PEP8 compliance to favour readability!
        # Load data from Github Repo
        with urllib.request.urlopen('https://raw.githubusercontent.com/co-map-v/co-map-v.github.io/main/data/ma_map.geojson') as response:   # pylint: disable=line-too-long
            counties_1 = json.load(response)
        wd_of_script = pathlib.Path(__file__).parent.absolute()
        filepath_read = os.path.join(wd_of_script, './', 'smoketest_data.csv')# pylint: disable=line-too-long
        df_time_1 = pd.read_csv(filepath_read)
        fig = app.death_counts_map(df_time_1,counties_1)
        string = str(type(fig))
        self.assertEqual(string, "<class 'plotly.graph_objs._figure.Figure'>")

    '''
    def smoke_test1(self):
        """Smoke Test: Death Counts Map

        Check if Plotly Express map code returns a choropleth map
        of arbitrarily determined death counts based on a dummy
        dataset. Each county unit is set to the same death count
        for each month. i.e. Month 1 = 0 deaths, Month 2 = 15 deaths,
        Month 3 = 30 deaths.

        Args:
            counties (GeoJSON)
            df_time (pandas dataframe): 'COUNTY' variable is a string.

        Returns:
            fig_death (Ploty figure)
        """
        #URLs left long, ouside of PEP8 compliance to favour readability!
        with open('ma_map_test.geojson') as response: # pylint: disable=line-too-long
            counties = json.load(response)

        df_time = pd.read_csv('smoketest_data.csv', dtype={'COUNTY': str}) # pylint: disable=line-too-long

        death_range_max = max(df_time.death_counts)
        fig_death = px.choropleth(df_time, geojson=counties, locations="COUNTY",
	        featureidkey='properties.NAME',
	        color="death_counts",
	        title="Number of COVID-19 Deaths in Massachusetts (USA) <br>"\
                "by County, January-March 2020",
	        labels={'death_counts':'Number of Deaths',
	            'condition_month':'Month'},
	        hover_name="COUNTY",
	        color_continuous_scale=px.colors.sequential.Reds,
	        range_color=[0,death_range_max],
	        animation_frame="condition_month")
        fig_death.update_geos(fitbounds="locations", visible=False)
        fig_death.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
        fig_death.show()

        self.assertTrue(fig_death)

    def smoke_test2(self):
        """Smoke Test: Case Count Map

        Check if Plotly Express map code returns a choropleth map
        of arbitrarily determined case counts based on a dummy
        dataset. Each county unit is set to the same death count
        for each month. i.e. Month 1 = 25 cases, Month 2 = 50 cases,
        Month 3 = 70 cases.

        Args:
            df_time
            counties

        Returns:
            fig_case (Ploty figure)
        """
        #URLs left long, ouside of PEP8 compliance to favour readability!
        with open('ma_map_test.geojson') as response: # pylint: disable=line-too-long
            counties = json.load(response)

        df_time = pd.read_csv('smoketest_data.csv', dtype={'COUNTY': str}) # pylint: disable=line-too-long

        pos_range_max = max(df_time.positive_counts)
        fig_case = px.choropleth(df_time, geojson=counties, locations="COUNTY",
	        featureidkey='properties.NAME',
	        color="positive_counts",
	        title="Number of Positive COVID-19 Cases in Massachusetts (USA) <br>"\
                "by County, January-March 2020",
	        labels={'positive_counts':'Number of Cases',
	            'condition_month':'Month'},
	        hover_name="COUNTY",
	        color_continuous_scale=px.colors.sequential.Blues,
	        range_color=[1,pos_range_max],
	        animation_frame="condition_month")
        fig_case.update_geos(fitbounds="locations", visible=False)
        fig_case.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
        fig_case.show()

        self.assertTrue(fig_case)
    '''
    
suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)
