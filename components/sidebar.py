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
                dbc.NavLink("Dashboard", className="bi bi-heart-pulse icsd",
                            href="/dashboard", active="exact"),
                            
                dbc.NavLink("O Projeto", className="bi bi-columns-gap icsd",
                            href="/oprojeto", active="exact"),

                dbc.NavLink("Integrantes", className="bi bi-people icsd",
                            href="/integrantes", active="exact"),
            ],   
        ),

         dbc.Button(
                    "Github", className="bi bi-github", external_link=True, target="_blank", href="https://github.com/anabeatrizzz/pi-quatro-univesp")

    ],className="sidebar")

