from dash import html
import dash_bootstrap_components as dbc

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

sidebar = html.Div(
    [
        html.Img(src="../assets/logo-univesp.png"),
        html.H2("PI - IV", className="display-4"),
        html.Hr(),
        html.P(
            "Análise de dados públicos da saúde sobre DSTs", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Dashboard", className="bi bi-house",
                            href="/dashboard", active="exact"),
                dbc.NavLink("O Projeto", className="bi bi-house",
                            href="/oprojeto", active="exact"),
                dbc.NavLink("Integrantes", className="bi bi-house",
                            href="/integrantes", active="exact"),
            ],
            vertical=True,
            pills=True,
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
                dbc.CardLink(
                    "Repositório", className="bi bi-github", href="#"),
            ]
        ),

    ],
    style=SIDEBAR_STYLE,
)
