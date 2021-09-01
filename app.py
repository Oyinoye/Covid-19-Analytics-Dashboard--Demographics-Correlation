import flask
import dash
import dash_bootstrap_components as dbc

# app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
# server = app.server

server = flask.Flask(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], server=server)