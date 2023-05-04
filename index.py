import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from pages import content, members, project
from components import accordion, sidebar

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
    title="Análise de dados públicos da saúde sobre DSTs",
    external_scripts=["/assets/plotly-locale-pt-br.js"]
)
app.scripts.config.serve_locally = True
app.title = 'PI - IV | DSTs'
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/dashboard" or pathname == "/":
        return accordion

    elif pathname == "/oprojeto":
        return project

    elif pathname == "/integrantes":
        return members

    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),  # type: ignore
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == '__main__':
    app.run_server(debug=True)
