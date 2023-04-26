from dash import html

project = html.Div([
    html.Section([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H4("O Projeto"),
                        html.P("Este Projeto Integrador propõe ilustrar a análise de dados sobre conjuntos de dados relacionados com DSTs. Para isso, irá utilizar dados públicos em escala, irá usufruir da plataforma Google Colab para auxiliar na criação das visualizações dos resultados e da linguagem de programação Python para criação do dashboard"),     
                    ], className="section-title"),

                ], className="col-xl-8 mx-auto text-center"),
            ], className="row"), 

        ], className="container"),

            html.Div([
                html.Div([
                    html.Ul([
                        html.Li([
                           html.Div([
                                html.Span(className="bi bi-stickies"),
                                html.H4("Brainstorm"),
                                html.P("We gather your business and products information. We then determine the direction of the project and understand your goals and we combine your ideas with ours for an amazing website."),
                           ], className="timeline_content"), 
                        ]),

                        html.Li([
                           html.Div([
                                html.Span(className="bi bi-lightbulb"),
                                html.H4("Discuss Ideas"),
                                html.P("We gather your business and products information. We then determine the direction of the project and understand your goals and we combine your ideas with ours for an amazing website."),
                           ], className="timeline_content"), 
                        ]),

                        html.Li([
                           html.Div([
                                html.Span(className="bi bi-boxes"),
                                html.H4("Make Project"),
                                html.P("We gather your business and products information. We then determine the direction of the project and understand your goals and we combine your ideas with ours for an amazing website."),
                           ], className="timeline_content"), 
                        ]),

                        html.Li([
                           html.Div([
                                html.Span(className="bi bi-wechat"),
                                html.H4("Select Strategy"),
                                html.P("We gather your business and products information. We then determine the direction of the project and understand your goals and we combine your ideas with ours for an amazing website."),
                           ], className="timeline_content"), 
                        ]),

                        html.Li([
                           html.Div([
                                html.Span(className="bi bi-bullseye"),
                                html.H4("Target"),
                                html.P("We gather your business and products information. We then determine the direction of the project and understand your goals and we combine your ideas with ours for an amazing website."),
                           ], className="timeline_content"), 
                        ]),

                        html.Li([
                           html.Div([
                                html.Span(className="bi bi-emoji-laughing"),
                                html.H4("Happy Costumers"),
                                html.P("We gather your business and products information. We then determine the direction of the project and understand your goals and we combine your ideas with ours for an amazing website."),
                           ], className="timeline_content"), 
                        ]),

                    ], className="timeline-list"),
                ], className="col-xl-12"),
            ], className="row"),

    ], className="experience pt-100 pb-100", id="experience"),

])