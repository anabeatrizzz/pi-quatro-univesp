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
                            csvList[c]["yColumn"])
                        )
                    ]),
                    title=csvList[c]["title"]
                ),
        )
    
    return accordionItems

accordion = html.Div([
            dbc.Accordion(
                getAccordionItems(),
                start_collapsed=True,
            )
        ])