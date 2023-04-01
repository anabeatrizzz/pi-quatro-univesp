# para iniciar a dash, no terminal inicie python index.py ele vai abrir no navegador http://127.0.0.1:8050/

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

import flask
import os
from flask import Flask

#importing required packages
import pandas as pd
from ydata_profiling import ProfileReport
import numpy as np

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
app.scripts.config.serve_locally = True

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

server = Flask(__name__)
STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.Img(src=app.get_asset_url('logo-univesp.png')),
        html.H2("PI - IV", className="display-4"),
        html.Hr(),
        html.P(
            "Analise de dados publico da saúde sobre DSTs", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Dashboard", className="bi bi-house", href="/dashboard", active="exact"),
                dbc.NavLink("O Projeto", className="bi bi-house", href="/oprojeto", active="exact"),
                dbc.NavLink("Integrantes", className="bi bi-house", href="/integrantes", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),  
        
        dbc.Card(
        [
            html.H4("O Projeto", className="card-title"),
            html.H6("Univesp - Eixo Computação", className="card-subtitle"),
            html.P(
                "Repositorio do Projeto "
                "Dashboard em Python",
                className="card-text",
            ),
            dbc.CardLink("Repositorio", className="bi bi-github", href="#"),
        ]
        ),

    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

#importing the data
csvSource = "https://raw.githubusercontent.com/anabeatrizzz/pi-quatro-univesp/master/tb-related-deaths-hiv.csv"
dfCSV = pd.read_csv(csvSource)
df_br = dfCSV[dfCSV['Entity'] == 'Brazil']

#descriptive statistics
#profile = ProfileReport(df_br)
#profile.to_file("test.html")

# Added
@app.server.route('/dashboard/<resource>')
def serve_static(resource):
    return flask.send_from_directory(STATIC_PATH, resource)

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/dashboard":
        return html.A('Navigate to nested web page', href='/assets/test.html'),
    elif pathname == "/oprojeto":
        return html.P("Aqui fica as informações do projeto!")
    elif pathname == "/integrantes":
        return html.P("Aqui fica as nossas informações!")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == '__main__':
    app.run_server(debug=True)