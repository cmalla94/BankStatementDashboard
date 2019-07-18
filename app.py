# main app file 

import dash 
import dash_html_components as html 

external_stylesheets = ['https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
layout = html.Div()
server = app.server
app.config['suppress_callback_exceptions']=True
