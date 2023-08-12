from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

import pandas as pd

app = Dash(__name__)

df = pd.read_csv('q.csv')

fig = px.scatter(df, x="date", y="Sales", color="date")
app.layout = html.Div([
    html.Div(children=[
        html.Label('Dropdown'),
        dcc.Dropdown(['North', 'South', 'East', 'West', 'all']),

        html.Br(),
        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(['North', 'South', 'East',
                      'West', 'all'],
                     multi=True),

        html.Br(),
        html.Label('Radio Items'),
        dcc.RadioItems(['North', 'South', 'East', 'West', 'all']),
    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        html.Label('Checkboxes'),
        dcc.Checklist(['North', 'South', 'East',
                       'West', 'all']
                      ),

        html.Br(),
        html.Label('Text Input'),
        dcc.Input(value='MTL', type='text'),

        dcc.Slider(
            df['region'],
            df['region'],
            step=None,
            id='region--slider',
            value=df['region'],
            marks={str('region'): str('region') for region in df['region'].unique()},
        ),
    ], style={'padding': 10, 'flex': 1})
], style={'display': 'flex', 'flex-direction': 'row'})

if __name__ == '__main__':
    app.run(debug=True)
