from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)
df=pd.read_csv('q.csv')
fig = px.line(df, x="date", y="Sales",line_group='date',color='date')
app.layout = html.Div(children=[
    html.H1(children='Chart'),

    html.Div(children='''
        Dash: Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021
    '''),
 dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
if __name__ == '__main__':
    app.run(debug=True)
