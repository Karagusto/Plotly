# -*- coding: utf-8 -*-


# Hello world of dash with plotly
# Basics to plot a dashboard

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background' : '#111111',
    'text' : '#7FDBFF'
}

app.layout = html.Div(children=[
    html.H1(children='EloDash',
            style={
                'textAlign' : 'center',
                'color' : colors['text']
            }
            ),

    html.Div(children='''Dash: Template for Elogroup.''',
             style={
                'textAlign' : 'center',
                'color' : colors['text']
             }
             ),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)