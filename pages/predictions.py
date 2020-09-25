# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load

# Imports from this application
from app import app
import pandas as pd
import sklearn

pipeline = load('assets/pipeline.joblib')
@app.callback(Output('prediction-content', 'children'),
             [Input('LILA', 'value'),
              Input('Fast_Food_Rest', 'value'),
              Input('Full_Serv_Rest', 'value'),
              Input('PC_FFRSALE', 'value'),
              Input('PC_FSRSALE', 'value'),
              Input('Grocery', 'value'),
              Input('Supermarket', 'value'),
              Input('Convenience', 'value'),
              Input('Specialty', 'value'),
              Input('Farmers_Market', 'value')])
def predict(LILA, Fast_Food_Rest, Full_Serv_Rest, PC_FFRSALE, PC_FSRSALE, Grocery, Supermarket, Convenience, Specialty, Farmers_Market):
    df = pd.DataFrame(
        columns=['LILA', 'Fast_Food_Rest', 'Full_Serv_Rest', 'PC_FFRSALE', 'PC_FSRSALE', 'Grocery', 'Supermarket', 'Convenience', 'Specialty', 'Farmers_Market'],
        data = [[LILA, Fast_Food_Rest, Full_Serv_Rest, PC_FFRSALE, PC_FSRSALE, Grocery, Supermarket, Convenience, Specialty, Farmers_Market]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'Average Obesity Rate is {y_pred:.2f}%'
    
# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown('## Local Availability in a County', className='mb-5'), 
        dcc.Markdown('#### Fast Food Restaurants per 1000 People'), 
        dcc.Slider(
            id='Fast_Food_Rest', 
            min=0, 
            max=6, 
            step=0.1, 
            value=0.8, 
            marks={n: str(n) for n in range(0,7,1)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Full Service Restaurants per 1000 People'), 
        dcc.Slider(
            id='Full_Serv_Rest', 
            min=0, 
            max=14, 
            step=0.1, 
            value=0.7, 
            marks={n: str(n) for n in range(0,15,2)}, 
            className='mb-5', 
        ),
        dcc.Markdown('#### Average $ Spent on Fast Food per Person in a Year'), 
        dcc.Slider(
            id='PC_FFRSALE', 
            min=300, 
            max=1150, 
            step=50, 
            value=619, 
            marks={
                300: '$300',
                500: '$500',
                700: '$700',
                900: '$900',
                1100: '$1100'
            }, 
            className='mb-5', 
        ),  
        dcc.Markdown('#### Average $ Spent on Full Service Restaurants per Person in a Year'), 
        dcc.Slider(
            id='PC_FSRSALE', 
            min=400, 
            max=2001, 
            step=50, 
            value=671, 
            marks={
                400: '$400',
                800: '$800',
                1200: '$1200',
                1600: '$1600',
                2000: '$2000'
            }, 
            className='mb-5', 
        ),        
    ],
    md=4,
)
column2 = dbc.Col(
    [
        dcc.Markdown('#### Population of Low Income, Low Access'), 
        dcc.Slider(
            id='LILA', 
            min=0, 
            max=70, 
            step=1, 
            value=1.73, 
            marks={
                0: '0%',
                10: '10',
                20: '20',
                30: '30',
                40: '40',
                50: '50',
                60: '60',
                70: '70%'
            }, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Grocery Stores per 1000 People'), 
        dcc.Slider(
            id='Grocery', 
            min=0, 
            max=3, 
            step=0.1, 
            value=0.28, 
            marks={n: str(n) for n in range(0,4,1)}, 
            className='mb-5',
        ),
        dcc.Markdown('#### Super Stores and Clubs per 1000 People'), 
        dcc.Slider(
            id='Supermarket', 
            min=0, 
            max=.25, 
            step=0.01, 
            value=.007, 
            marks={
                0: '0',
                0.05: '0.05',
                0.1: '0.10',
                0.15: '0.15',
                0.2: '0.20',
                0.25: '0.25'
            },
            className='mb-5',
        ),
        dcc.Markdown('#### Convenience Stores per 1000 People'), 
        dcc.Slider(
            id='Convenience', 
            min=0, 
            max=3.5, 
            step=0.25, 
            value=0.254, 
            marks={
                0: '0',
                0.5: '0.5',
                1: '1.0',
                1.5: '1.5',
                2: '2.0',
                2.5: '2.5',
                3: '3.0',
                3.5: '3.5'
            }, 
            className='mb-5',
        ),
        dcc.Markdown('#### Specialty Markets per 1000 People'), 
        dcc.Slider(
            id='Specialty', 
            min=0, 
            max=1, 
            step=0.1, 
            value=.084, 
            marks={
                0: '0',
                0.2: '0.2',
                0.4: '0.4',
                0.6: '0.6',
                0.8: '0.8',
                1.0: '1.0'
            }, 
            className='mb-5',
        ),
        dcc.Markdown('#### Farmers Markets per 1000 People'), 
        dcc.Slider(
            id='Farmers_Market', 
            min=0, 
            max=1.0, 
            step=0.1, 
            value=.018, 
            marks={
                0: '0',
                0.2: '0.2',
                0.4: '0.4',
                0.6: '0.6',
                0.8: '0.8',
                1.0: '1.0'
            },
            className='mb-5',
        ),        
    ],
    md=4,
)

column3 = dbc.Col(
    [
        html.H2('Predicted Changes in the Average Obesity Rate:', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2, column3])