# para iniciar a dash, no terminal inicie python index.py ele vai abrir no navegador http://127.0.0.1:8050/

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

import os

#importing required packages
import pandas as pd
from ydata_profiling import ProfileReport
import numpy as np
import plotly.express as px

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

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/dashboard" or pathname == "/" :
        csvSource = "https://raw.githubusercontent.com/anabeatrizzz/pi-quatro-univesp/master/tb-related-deaths-hiv.csv"
        dfCSV = pd.read_csv(csvSource)
        dfCSV.rename(
        columns={
            "Entity": "Entity",
            "Code": "Code",
            "Year": "Ano",
            "Estimated TB-related deaths among people living with HIV - estimate": "Mortes estimadas"
        },
        inplace=True
    )
        df_br = dfCSV[dfCSV['Entity'] == 'Brazil']
        
        fig = px.scatter(df_br, x="Ano", y="Mortes estimadas")
        return html.Div(
            [
                html.B("Mortes estimadas relacionadas à tuberculose entre pessoas vivendo com HIV por ano"),
                html.Div([ dcc.Graph(figure=fig) ])
            ]
        )
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