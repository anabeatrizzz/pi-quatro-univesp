from dash import html


def getMemberParagraph():
    membersListParagraph = []
    membersList = [
        "Abner Veloso Bezerra | E-mail: 1701120@aluno.univesp.br",
        "Alan Alves da Silva | E-mail: 2002522@aluno.univesp.br",
        "Ana Beatriz Augusto de Melo da Silva | E-mail: 2004708@aluno.univesp.br",
        "Clovis Garcia | E-mail: 2006404@aluno.univesp.br",
        "Isabella De Oliveira Tolentino | E-mail: 2002812@aluno.univesp.br",
        "Lucas Dos Santos Dias | E-mail: 2000549@aluno.univesp.br",
        "Rafael Fortes Gatto | E-mail: 2014805@aluno.univesp.br",
        "Rodrigo Sanches Gamboa | E-mail: 2002899@aluno.univesp.br"
    ]

    for c in range(len(membersList)):
        membersListParagraph.append(
            html.P(membersList[c])
        )

    return membersListParagraph


members = html.Div(
    [
        html.B("A equipe é composta por:"),
        html.Br(),
        html.Br(),
        html.Div(getMemberParagraph())
    ]
)
