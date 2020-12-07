"""CO-MAP-V Application Code

Functions:
 	death_counts_map(df_time,counties)
 	case_count_map(df_time,counties)
 	population_map(df_time,counties)
 	deaths_histogram(df)
 	case_histogram(df)
 	population_histogram(df)
 	create_tabs(tabs_content:list)

Args:
	df_time (pandas dataframe): Dataset containing county-level
	OMOP Synthetic COVID-19 and demographic data for Massachusetts.
	counties (GeoJSON): GeoJSON file containing shape of counties
	in Massachusetts.
"""

# CSE 583 Final Project
# Languages: Python, HTML
# Code Style: PEP8
# Authors: Aja Sutton, Andrew Teng, Jason Thomas, Nanhsuan Yuan
# Autumn 2020


import dash
import json
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import urllib.request


def death_counts_map(df_time,counties):
    """Death Counts Map

    Reads in a GeoJSON file and a demographics CSV file.
    Generates a choropleth map of COVID-19 death counts by county for
    the state of Massachusetts. Includes an interactive time slider
    based on month of the year.

    Args:
    	counties (GeoJSON)
    	df_time (pandas dataframe): 'COUNTY' variable set to string.

    Returns:
    	fig_death (Ploty Express figure)
    """
    death_range_max = max(df_time.death_counts)
    fig_death = px.choropleth(df_time, geojson=counties, locations="COUNTY",
	featureidkey='properties.NAME',
	color="death_counts",
	title="Number of COVID-19 Deaths in Massachusetts (USA) <br> by County, January-March 2020",
	labels={'death_counts':'Number of Deaths',
		'condition_month':'Month'},
	hover_name="COUNTY",
	color_continuous_scale=px.colors.sequential.Reds,
	range_color=[0,death_range_max],
	animation_frame="condition_month")
    fig_death.update_geos(fitbounds="locations", visible=False)
    fig_death.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
    return fig_death


def case_count_map(df_time,counties):
    """Case Count Map

    Reads in a GeoJSON file and a demographics CSV file.
    Generates a choropleth map of positive COVID-19 case counts by
    county for the state of Massachusetts. Includes an interactive
    timeslider based on month of the year.

    Args:
    	df_time
    	counties

    Returns:
    	fig_case (Ploty Express figure)
    """
    pos_range_max = max(df_time.positive_counts)
    fig_case = px.choropleth(df_time, geojson=counties, locations="COUNTY",
	featureidkey='properties.NAME',
	color="positive_counts",
	title="Number of Positive COVID-19 Cases in Massachusetts (USA) <br> by County, January-March 2020",
	labels={'positive_counts':'Number of Cases',
		'condition_month':'Month'},
	hover_name="COUNTY",
	color_continuous_scale=px.colors.sequential.Blues,
	range_color=[1,pos_range_max],
	animation_frame="condition_month")
    fig_case.update_geos(fitbounds="locations", visible=False)
    fig_case.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
    return fig_case


def population_map(df_time,counties):
    """Population Map

    Reads in a GeoJSON file and a demographics CSV file.
    Generates a choropleth map of population density by
    county for the state of Massachusetts.

      Args:
    	df_time
    	counties

    Returns:
    	fig_pop (Ploty Express figure)
    """
    pos_range_max = max(df_time.population_2010)
    fig_pop = px.choropleth(df_time, geojson=counties, locations="COUNTY",
	featureidkey='properties.NAME',
	color="population_2010",
	title="Population by County, Massachusetts (USA), 2010 Census",
	labels={'population_2010':'Population',
		'condition_month':'Month'},
	hover_name="COUNTY",
	color_continuous_scale=px.colors.sequential.Greens,
	range_color=[1,pos_range_max])
    fig_pop.update_geos(fitbounds="locations", visible=False)
    fig_pop.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
    return fig_pop


def deaths_histogram(df):
    """Deaths Histogram
	
	Args:
    	df (pandas dataframe): df_time pandas dataframe read in as "df".
    """
    fig_death_hist = px.histogram(df, x="COUNTY" , y="death_counts", 
    title="Number of COVID-19 Deaths in Massachusetts (USA) <br> by County, January-March 2020",
    labels={'population_2010':'Population',
        'condition_month':'Month'},
     animation_frame="condition_month")

    fig_death_hist.update_layout(
        xaxis_title_text='County', # xaxis label
        yaxis_title_text='Total Deaths', # yaxis label
    )
    return fig_death_hist


def case_histogram(df):
    """Cases Histogram

	Args:
    	df (pandas dataframe)
    """
    fig_cases_hist = px.histogram(df, x="COUNTY" , y="positive_counts", 
    title="Number of Positive COVID-19 Cases in Massachusetts (USA) <br> by County, January-March 2020",
    labels={'population_2010':'Population',
        'condition_month':'Month'},
     animation_frame="condition_month")

    fig_cases_hist.update_layout(
        xaxis_title_text='County', # xaxis label
        yaxis_title_text='Total Cases', # yaxis label
    )
    return fig_cases_hist


def population_histogram(df):
    """Population Histogram

	Args:
    	df (pandas dataframe)
    """
    fig_pop_hist = px.histogram(df, x="COUNTY" , y="population_2010", 
    title="Population by County, Massachusetts (USA), 2010 Census",
    labels={'population_2010':'Population'},)

    fig_pop_hist.update_layout(
        xaxis_title_text='County', # xaxis label
        yaxis_title_text='Population', # yaxis label
    )
    return fig_pop_hist


def create_tabs(tabs_content:list):
    """Bootstrap Tabs

    Declares the tabs using Bootstrap and Dash.

    Args:
    	tabs_content (list)
    """
    tabs = dbc.Tabs(
    [
        dbc.Tab(tabs_content[0], label="Cases (Map)"),
        dbc.Tab(tabs_content[1], label="Deaths (Map)"),
        dbc.Tab(tabs_content[2], label="Population (Map)"),
        dbc.Tab(tabs_content[3], label="Cases (Chart)"),
        dbc.Tab(tabs_content[4], label="Deaths (Chart)"),
        dbc.Tab(tabs_content[5], label="Population (Chart)"),
    ])
    return tabs


# Load data from Github Repo
with urllib.request.urlopen('https://raw.githubusercontent.com/co-map-v/co-map-v.github.io/main/data/ma_map.geojson') as response:
    counties = json.load(response)
df_time = pd.read_csv('https://raw.githubusercontent.com/co-map-v/co-map-v.github.io/main/data/covid_ma_positive_death_counts.csv',
dtype={'COUNTY': str})


#Initialize figures/maps and histograms
fig_death = death_counts_map(df_time,counties)
fig_case = case_count_map(df_time,counties)
fig_pop = population_map(df_time,counties)

fig_death_hist = deaths_histogram(df_time)
fig_case_hist = case_histogram(df_time)
fig_pop_hist = population_histogram(df_time)

figs = [fig_case,fig_death,fig_pop,fig_case_hist,fig_death_hist,fig_pop_hist]


# Tab Content
tabs_content = []

for i in range(len(figs)):
    # Describes the content within the tabs. Injects HTML formatted graphs
    # into the tab window space.
    tabs_content.append(dbc.Card(dbc.CardBody([html.Div(dcc.Graph(figure=figs[i],))]),))

tabs = create_tabs(tabs_content)
# Formats the layout of the Dash dashboard. Imports the Bootstrap and
# Dash theme
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(tabs)
server = app.server


# Starts local server
if __name__ == "__main__":
    app.run_server(debug=True)
