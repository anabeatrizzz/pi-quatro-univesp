from dash import html

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

        html.Button(["Rodrigo Sanches Gamboa"], className="link", id="btn"),
        html.Button(["Ana Beatriz"], className="link", id="btn"),
        html.Button(["Clovis Garcia"], className="link", id="btn"),
        html.Button(["Isabella De Oliveira"], className="link", id="btn"),
        html.Button(["Rafael Fortes"], className="link", id="btn"),
        html.Button(["Abner Veloso"], className="link", id="btn"),
        html.Button(["Alan Alves"], className="link", id="btn"),
        html.Button(["Lucas Dos Santos"], className="link", id="btn"), 

        ], className="container"),
        
    ], className="experience pt-100 pb-100", id="experience"),
])