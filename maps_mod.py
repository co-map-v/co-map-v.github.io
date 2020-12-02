# CO-MAP-V Maps
# Contains three functions corresponding to Plotly
# -based choropleth maps of synthetic data-based COVID-19 death counts,
# positive COVID-19 counts, and overall population density by county for
# the state of Massachusetts, January-March 2020. Maps include
# interactive timesliders. Data are imported locally.

# Data Input:
	# GeoJSON file: located at './map.geojson'.
	# CSV file: located at './data/covid_ma_positive_death_counts.csv'.

# CSE 583 Final Project
# Authors: Aja Sutton, Andrew Teng, Jason Thomas, Nanhsuan Yuan
# Autumn 2020


import json
import plotly.express as px
import pandas as pd
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
#from dash.dependencies import Input, Output


# Death Counts Map

# Reads in a GeoJSON file and a demographics CSV file.
# Generates a choropleth map of COVID-19 death counts by county for
# the state of Massachusetts. Includes an interactive time slider
# based on month of the year.

with open('data/ma_map.geojson', 'r') as response:
    counties = json.load(response)

df_time = pd.read_csv('data/covid_ma_positive_death_counts.csv',
	dtype={'COUNTY': str})

fig_death = px.choropleth(df_time, geojson=counties, locations="COUNTY",
	featureidkey='properties.NAME',
	color="death_counts",
	title="Number of COVID-19 Deaths in Massachusetts (USA) by " +
		"County, January-March 2020",
	labels={'death_counts':'Number of Deaths',
		'condition_month':'Month'},
	hover_name="COUNTY",
	color_continuous_scale=px.colors.sequential.Blues,
	range_color=[0,30],
	animation_frame="condition_month")
fig_death.update_geos(fitbounds="locations", visible=False)
fig_death.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
#fig.show()


# Case Count Map

# Reads in a GeoJSON file and a demographics CSV file.
# Generates a choropleth map of positive COVID-19 case counts by
# county for the state of Massachusetts. Includes an interactive
# timeslider based on month of the year.

with open('data/ma_map.geojson', 'r') as response:
    counties = json.load(response)

df_time = pd.read_csv('data/covid_ma_positive_death_counts.csv',
	dtype={'COUNTY': str})

fig_case = px.choropleth(df_time, geojson=counties, locations="COUNTY",
	featureidkey='properties.NAME',
	color="positive_counts",
	title="Number of Positive COVID-19 Cases in Massachusetts (USA)"
		+ " by County, January-March 2020",
	labels={'positive_counts':'Number of Cases',
		'condition_month':'Month'},
	hover_name="COUNTY",
	color_continuous_scale=px.colors.sequential.Blues,
	range_color=[1,70],
	animation_frame="condition_month")
fig_case.update_geos(fitbounds="locations", visible=False)
fig_case.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
#fig.show()


# Population Map

# Reads in a GeoJSON file and a demographics CSV file.
# Generates a choropleth map of population density by
# county for the state of Massachusetts.

with open('data/ma_map.geojson', 'r') as response:
    counties = json.load(response)

df_time = pd.read_csv('data/covid_ma_positive_death_counts.csv',
	dtype={'COUNTY': str})

fig_pop = px.choropleth(df_time, geojson=counties, locations="COUNTY",
	featureidkey='properties.NAME',
	color="population_2010",
	title="Population by County, Massachusetts (USA), " +
		"January-March 2020",
	labels={'population_2010':'Population',
		'condition_month':'Month'},
	hover_name="COUNTY",
	color_continuous_scale=px.colors.sequential.Blues,
	range_color=[1,800000])
fig_pop.update_geos(fitbounds="locations", visible=False)
fig_pop.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
#fig.show()


# Graph IDs

# Assign identifiers to plotly graph figures and formats them with Dash
# them with Dash components

graph1 = dcc.Graph(
    id='graph1',
    figure=fig_death,
    className="six columns"
)
graph2 = dcc.Graph(
    id='graph2',
    figure=fig_case,
    className="six columns"
    )
graph3 = dcc.Graph(
    id='graph3',
    figure=fig_pop,
    className="six columns"
    )


# Tab Content

# Describes the content within the tabs. Injects HTML formatted graphs
# into the tab window space.

tab1_content = dbc.Card(
    dbc.CardBody([html.Div(graph1)]),
    className="mt-3",
)
tab2_content = dbc.Card(
    dbc.CardBody([html.Div(graph3)]),
    className="mt-3",
)
tab3_content = dbc.Card(
    dbc.CardBody([html.Div(graph2)]),
    className="mt-3",
)

# Bootstrap Tabs

# Declares the tabs using Bootstrap and Dash

tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Cases (Map)"),
        dbc.Tab(tab2_content, label="Deaths (Map)"),
        dbc.Tab(tab3_content, label="Population (Map)"),
    ]
)

# Formats the layout of the Dash dashboard. Imports the Bootstrap and
# Dash theme
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(tabs)

# Starts local server
if __name__ == "__main__":
    app.run_server(debug=True)