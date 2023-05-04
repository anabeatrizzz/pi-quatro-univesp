from dash import html
import dash_mantine_components as dmc

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

mobilecontent = html.Div(
    id="page-content"
)

webcontent = html.Div(
    id="page-content",
    style=CONTENT_STYLE
)

content = html.Div(
    [
        dmc.MediaQuery(
            [webcontent],
            smallerThan="sm",
            styles=CONTENT_STYLE
        ),
        dmc.MediaQuery(
            [mobilecontent],
            largerThan="sm",
            styles=CONTENT_STYLE
        ),
    ]
)
