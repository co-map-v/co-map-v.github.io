"""CO-MAP-V Maps Module contains three functions that correspond to Plotly-based choropleth maps of synthetic data-based COVID-19 death counts, positive COVID-19 counts, and overall population density by county for the state of Massachusetts, January-March 2020. Maps include interactive timesliders. Data are imported locally.

Functions:
	death_counts()
	positive_counts()
	population_map()

Data Requirements:
	GeoJSON file: located at './map.geojson'.
	CSV file: located at './data/covid_ma_positive_death_counts.csv'.
"""

# CSE 583 Final Project
# Authors: Aja Sutton, Andrew Teng, Jason Thomas, Nanhsuan Yuan
# Autumn 2020


import plotly.express as px
import pandas as pd
import numpy as np
import json


def death_counts():
	"""Reads in a GeoJSON file and a demographics CSV file.
	Generates a choropleth map of COVID-19 death counts by county for the state of Massachusetts. Includes an interactive time slider based on month of the year.

	Args: 
		None

	Returns:
		fig: shows a Plotly Express-based interactive choropleth map.
	""" 
	with open('./map.geojson', 'r') as response:
	    counties = json.load(response)

	df_time = pd.read_csv('./data/covid_ma_positive_death_counts.csv',
	                   dtype={'COUNTY': str})

	fig = px.choropleth(df_time, geojson=counties, locations="COUNTY",
						featureidkey='properties.NAME',
	                    color="death_counts",
	                    title="Number of COVID-19 Deaths in Massachusetts (USA) by County, January-March 2020",
	                    labels={'death_counts':'Number of Deaths', 'condition_month':'Month'},
	                    hover_name="COUNTY", 
	                    color_continuous_scale=px.colors.sequential.Blues,
	                    range_color=[0,30],
	                    animation_frame="condition_month")
	fig.update_geos(fitbounds="locations", visible=False)
	fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
	fig.show()


def positive_counts():
	"""Reads in a GeoJSON file and a demographics CSV file.
	Generates a choropleth map of positive COVID-19 case counts by
	county for the state of Massachusetts. Includes an interactive time slider based on month of the year.

	Args: 
		None

	Returns:
		fig: shows a Plotly Express-based interactive choropleth map.
	"""
	with open('./map.geojson', 'r') as response:
    counties = json.load(response)

	df_time = pd.read_csv('./data/covid_ma_positive_death_counts.csv',
	                   dtype={'COUNTY': str})

	fig = px.choropleth(df_time, geojson=counties, locations="COUNTY", featureidkey='properties.NAME',
	                    color="positive_counts",
	                    title="Number of Positive COVID-19 Cases in Massachusetts (USA) by County, January-March 2020",
	                    labels={'positive_counts':'Number of Cases', 'condition_month':'Month'},
	                    hover_name="COUNTY", 
	                    color_continuous_scale=px.colors.sequential.Blues,
	                    range_color=[1,70],
	                    animation_frame="condition_month")
	fig.update_geos(fitbounds="locations", visible=False)
	fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
	fig.show()

def population_map():
	"""Reads in a GeoJSON file and a demographics CSV file.
	Generates a choropleth map of population density by
	county for the state of Massachusetts.

	Args: 
		None

	Returns:
		fig: shows a Plotly Express-based interactive choropleth map.
	"""
	with open('./map.geojson', 'r') as response:
    counties = json.load(response)

	df_time = pd.read_csv('./data/covid_ma_positive_death_counts.csv',
	                   dtype={'COUNTY': str})

	fig = px.choropleth(df_time, geojson=counties, locations="COUNTY", featureidkey='properties.NAME',
	                    color="population_2010",
	                    title="Population by County, Massachusetts (USA), January-March 2020",
	                    labels={'population_2010':'Population', 'condition_month':'Month'},
	                    hover_name="COUNTY", 
	                    color_continuous_scale=px.colors.sequential.Blues,
	                    range_color=[1,800000])
	fig.update_geos(fitbounds="locations", visible=False)
	fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
	fig.show()