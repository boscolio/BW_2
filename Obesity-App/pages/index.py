# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Can we use Stores and Restaurants to predict Obesity?

            PON is an app that tries to predict obesity based on restaurants and food stores in a county.  Have you ever wondered what can happen when your local fruit market closes and the "golden arches" move in?

            """
        ),
        dcc.Link(dbc.Button('Predict Obesity Now!', color='primary'), href='/predictions')
    ],
    md=4,
)


layout = dbc.Row([column1])