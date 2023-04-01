from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB,
                                           dbc.icons.BOOTSTRAP])


card_world = dbc.Card(
    dbc.CardBody(
        [
            html.H1([html.I(className="bi bi-globe sm-2"),
                     ], className="text-nowrap"),
            html.H3("Total World"),
            html.Div(
                [html.I("12.935",
                    className="fs-2 fw-bold"),
                ]
            ),
        ], className="card text-white bg-primary"
    ),
    className="text-center m-4"
)


card_live = dbc.Card(
    dbc.CardBody(
        [
            html.H1([html.I(className="bi bi-person-up me-2"), ],
                    className="text-nowrap"),
            html.H3("Lives HIVs",),
            html.Div(
                [
                    html.I("12.3%",
                    className="fs-2 fw-bold"),
                ]
            ),
        ], className="card text-white bg-primary"
    ),
    className="text-center m-4",
)


card_die = dbc.Card(
    dbc.CardBody(
        [
            html.H1([html.I(className="bi bi-person-down me-2"), ],
                    className="text-nowrap"),
            html.H3("Die HIVs"),
            html.Div(
                [
                 html.I("10.3%",
                     className="fs-2 fw-bold"),
                ]
            ),
        ], className="card text-white bg-primary"
    ),
    className="text-center m-4",
)

card_kids = dbc.Card(
    dbc.CardBody(
        [
            html.H1([html.I(className="bi bi-activity me-2"), ],
                    className="text-nowrap"),
            html.H3("Kids HIVs"),
            html.Div(
                [
                 html.I("10.3%",
                     className="fs-2 fw-bold"),
                ]
            ),
        ], className="card text-white bg-primary"
    ),
    className="text-center m-4",
)


app.layout = dbc.Container(
    dbc.Row(
        [dbc.Col(card_world), dbc.Col(card_live),
         dbc.Col(card_die), dbc.Col(card_kids)],
    ),
    fluid=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)