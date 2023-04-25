from dash import html
import dash_bootstrap_components as dbc

sidebar = html.Div(
    [
        html.Img(src="../assets/logo-univesp-white.png", className="logo"),
        html.H2("PI - IV", className="sub-tt"),
        html.P(
            "Análise de dados públicos da saúde sobre DSTs", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Dashboard", className="bi bi-heart-pulse",
                            href="/dashboard", active="exact"),
                            
                dbc.NavLink("O Projeto", className="bi bi-columns-gap",
                            href="/oprojeto", active="exact"),

                dbc.NavLink("Integrantes", className="bi bi-people",
                            href="/integrantes", active="exact"),
            ],   
        ),

        dbc.Card(
            [
                html.H4("O Projeto", className="card-title"),
                html.H6("Univesp - Eixo Computação",
                        className="card-subtitle"),
                html.P(
                    "Repositório do Projeto "
                    "Dashboard em Python",
                    className="card-text",
                ),
                dbc.Button(
                    "Repositório", className="bi bi-github", external_link=True, target="_blank", href="https://github.com/anabeatrizzz/pi-quatro-univesp"),
            ]
        ),

    ],className="sidebar")
