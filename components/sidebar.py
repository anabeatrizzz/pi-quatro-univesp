from dash import html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

INNERBOXSTYLE = {"width": "auto"}
MEDIAQUERYSTYLES = {"display": "none", "width": "auto"}

sidebarcontent = [
    html.Img(src="https://raw.githubusercontent.com/anabeatrizzz/pi-quatro-univesp/master/assets/logo-univesp-white.png", className="logo"),
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

]

websidebar = html.Div(
    sidebarcontent,
    className="sidebar"
)

mobilesidebar = dbc.NavbarSimple(
    sidebarcontent,
    color="bs-blue",
    class_name="mobilesidebar"
)

sidebar = html.Div(
    [
        dmc.MediaQuery(
            [websidebar],
            innerBoxStyle=INNERBOXSTYLE,
            smallerThan="sm",
            styles=MEDIAQUERYSTYLES,
        ),
        dmc.MediaQuery(
            [mobilesidebar],
            largerThan="sm",
            innerBoxStyle=INNERBOXSTYLE,
            styles=MEDIAQUERYSTYLES,
        ),
    ]
)
