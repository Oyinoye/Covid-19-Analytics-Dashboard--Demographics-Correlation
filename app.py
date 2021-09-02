import flask
import dash
import dash_bootstrap_components as dbc
import os

# app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
# server = app.server

server = flask.Flask(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], server=server)
server.secret_key = os.environ.get('secret_key', 'secret')