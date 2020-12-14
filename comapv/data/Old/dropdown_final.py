'''
This is the module for a dropdown bar chart for counts of positives
by counts by month. The dropdown box is month
'''

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.offline as pyo
import plotly.graph_objs as go
from dash.dependencies import Input, Output

APP = dash.Dash()

#read in the data
DF = pd.read_csv('/data/features_by_month_and_county.csv')

#setup the dropdown options
DF = DF.sort_values(by='condition_month', ascending = True) #sorting by month for the dictionary below
MONTH_OPTIONS = []
#determining the unique options for months and making a dictionary for their dropdown
for month in DF['condition_month'].unique():
    MONTH_OPTIONS.APPend({'label':(f'month: {month}'),'value':month})

#re-sort the data by positive counts sum so that the bars are sorted below
DF = DF.sort_values(by='positive_counts_sum', ascending = False)

APP.layout = html.Div([
    dcc.Graph(id='graph-with-dropdown'),
    dcc.Dropdown(id='month-picker',options=MONTH_OPTIONS,value=DF['condition_month'].min())
])

@APP.callback(Output('graph-with-dropdown', 'figure'),
              [Input('month-picker', 'value')])
def update_figure(selected_month):
    '''This function creates a bar chart for each month

    Args:
        selected_month (str): the only parameter

    Returns:
        A bar chart for the specific month
    '''
    filtered_DF = DF[DF['condition_month'] == selected_month] #filters the month to the specific month
    #traces = []

    return {'data': [go.Bar(
                x=filtered_DF['county'],  # the specific county
                y=filtered_DF['positive_counts_sum'] #counts of positive tests
                )
            ],
            'layout': go.Layout(
                title='Total positive tests per county by month' #title
                )
    }
    #fig = go.Figure(data=data, layout=layout)

if __name__ == '__main__':
    APP.run_server()
