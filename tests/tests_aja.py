import json
import plotly.express as px

#Smoke tests data loaded as global variables to avoid redownloading
with open('./data/ma_map.geojson', 'r') as response:
	counties = json.load(response)

df_time = pd.read_csv('./tests/smoketest_data.csv',
	dtype={'COUNTY': str})

def smoke_test1(df_time,counties):
    """Smoke Test: Death Counts Map

    Check if Plotly Express map code returns a choropleth map
    of arbitrarily determined death counts based on a dummy
    dataset. Each county unit is set to the same death count
    for each month. i.e. Month 1 = 0 deaths, Month 2 = 15 deaths,
    Month 3 = 30 deaths.

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

def smoke_test2(df_time,counties):
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
