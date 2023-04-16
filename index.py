import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from pages import content
from components import accordion, sidebar

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
app.scripts.config.serve_locally = True

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/dashboard" or pathname == "/":
        return accordion

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