from dash import Dash, html, dcc
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

slide_year = html.Div([
    dcc.RangeSlider(0, 3,
        id='non-linear-range-slider',
        marks={i: '{}'.format(10 ** i) for i in range(4)},
        value=[0.1, 2],
        dots=False,
        step=0.01,
        updatemode='drag'
    ),
    html.Div(id='output-container-range-slider-non-linear', style={'margin-top': 20})
])

app.layout = dbc.Container(
    dbc.Row(
        [dbc.Col(card_world), dbc.Col(card_live),
         dbc.Col(card_die), dbc.Col(card_kids)],
    ),
    fluid=True,
)


# app.layout = html.Div([slider, dcc.Graph(id="graph")]) 

if __name__ == "__main__":
    app.run_server(debug=True)