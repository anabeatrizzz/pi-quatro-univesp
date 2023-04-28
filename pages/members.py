from dash import html


def getMembersList():
    membersList = [
        "Rodrigo Sanches Gamboa",
        "Ana Beatriz",
        "Clovis Garcia",
        "Isabella De Oliveira",
        "Rafael Fortes",
        "Abner Veloso",
        "Alan Alves",
        "Lucas Dos Santos"
    ]

    buttonItems = []

    for name in membersList:
        buttonItems.append(
            html.Button([name], className="link members-btn", id=name),
        )
    return buttonItems


members = html.Div([
    html.Section([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H4("A Equipe"),
                        html.P("A Dashboard desnvolvido pelos alunos da disciplina de Projeto Integrador IV para o Eixo de Computação da Universidade Virtual do Estado de São Paulo (UNIVESP)."),
                    ], className="section-title"),

                ], className="col-xl-8 mx-auto text-center"),

            ], className="row"),

            html.Div(getMembersList()),

        ], className="container"),

    ], className="experience pt-100 pb-100", id="experience"),
])
