import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load sales data from CSV
sales_data = pd.read_csv('q.csv')

# Create a Dash app instance
app = dash.Dash(__name__)

# Define app layout with CSS styling
app.layout = html.Div(style={'font-family': 'Arial, sans-serif', 'text-align': 'center', 'margin': '50px'},
                      children=[
                          html.H1("Pink Morsels Sales Data", style={'margin-bottom': '20px'}),

                          dcc.RadioItems(
                              id='region-radio',
                              options=[
                                  {'label': 'North', 'value': 'north'},
                                  {'label': 'East', 'value': 'east'},
                                  {'label': 'South', 'value': 'south'},
                                  {'label': 'West', 'value': 'west'},
                                  {'label': 'All', 'value': 'all'}
                              ],
                              value='all',
                              labelStyle={'display': 'block', 'margin': '10px auto'}
                          ),

                          dcc.Graph(id='sales-graph', style={'width': '80%', 'margin': '20px auto'})
                      ]
                      )


# Define callback to update the graph based on radio button selection
@app.callback(
    Output('sales-graph', 'figure'),
    [Input('region-radio', 'value')]
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_data = sales_data
    else:
        filtered_data = sales_data[sales_data['region'] == selected_region]

    fig = px.line(filtered_data, x='date', y='Sales', title=f'Sales Data for {selected_region.capitalize()} region')
    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)



