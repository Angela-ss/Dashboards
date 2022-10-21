# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# https://dash.plotly.com/installation - Tutorial

import openpyxl
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("chamados.xlsx")

fig = px.histogram(df, x="STATUS", color="STATUSSLA", barmode="group", text_auto=True, facet_col="ATRIBUID")

app.layout = html.Div(children=[

    html.H1(children='Chamados'),

    html.Div(children='Dash: Aplicação web para visualização de chamados.'),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    ),

    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'



if __name__ == '__main__':
    app.run_server(debug=True)