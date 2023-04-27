import dash_bootstrap_components as dbc
from dash import dcc, html
from assets.csvList import csvList
import pandas as pd
import plotly.express as px


def getGraph(csvSource, newColumnsNames, xName, yName):
    df = pd.read_csv(csvSource)
    if newColumnsNames:
        df.rename(columns=newColumnsNames, inplace=True)

    newDF = df[df['Entity'] == 'Brazil']
    fig = px.scatter(newDF, x=xName, y=yName)

    return fig


def getAccordionItems():
    accordionItems = []

    for c in range(len(csvList)):
        accordionItems.append(
            dbc.AccordionItem(
                html.Div([
                    dcc.Graph(
                        figure=getGraph(csvList[c]["csvSource"],
                                        csvList[c]["newColumnsNames"],
                                        csvList[c]["newColumnsNames"]["Year"],
                                        csvList[c]["yColumn"]),
                        config={"locale": 'pt-br'},
                    )
                ]),
                title=csvList[c]["title"]
            ),
        )

    return accordionItems


accordion = html.Div([
    html.Section([    
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H4("Dashboard"),
                    ], className="section-title"),

                ], className="col-xl-8 mx-auto text-center"),

          ], className="row"),

        dbc.Accordion(
        getAccordionItems(),
        start_collapsed=True,
        )
        
    ], className="container"),
        
    ], className="experience pt-100 pb-100", id="experience"),
])
