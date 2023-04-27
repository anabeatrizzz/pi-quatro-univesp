from dash import html

project = html.Div([
    html.Section([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H4("O Projeto"),
                        html.P("Este Projeto Integrador propõe ilustrar a análise de dados sobre conjuntos de dados relacionados com DSTs. Para isso, irá utilizar dados públicos em escala, irá usufruir da plataforma Google Colab para auxiliar na criação das visualizações dos resultados e da linguagem de programação Python para criação do dashboard."),
                    ], className="section-title"),

                ], className="col-xl-8 mx-auto text-center"),
            ], className="row"), 

        ], className="container"),

            html.Div([
                html.Div([
                    html.Ul([
                        html.Li([
                           html.Div([
                                html.Span(className="bi bi-people-fill"),
                                html.H4("Empatia"),
                                html.P("Utilizando a ementa deste Projeto Integrador, que cita os assuntos Resolução de Problemas e Visualização de Dados, em conjunto com discussões entre a equipe sobre qual assunto específico seria abordado, a pergunta que guiará o desenvolvimento da pesquisa será: Como um dashboard web pode ajudar a divulgar informações sobre Doenças Sexualmente Transmissíveis (DSTs) para qualquer pessoa interessada?"),
                           ], className="timeline_content"), 
                        ]),

                        html.Li([
                           html.Div([
                                html.Span(className="bi bi-lightbulb"),
                                html.H4("Definição"),
                                html.P("O projeto consistirá em uma análise de dados que será desenvolvida em formato dashboard correlacionando as informações da área da saúde, especificamente sobre Doenças Sexualmente Transmissíveis (DSTs). Verificou-se a existência de diversos dados relacionados às DSTs, mas em formatos nada fáceis para uma pessoa conseguir entender sobre o assunto."),
                           ], className="timeline_content"), 
                        ]),

                        html.Li([
                           html.Div([
                                html.Span(className="bi bi-stickies"),
                                html.H4("Idealizar"),
                                html.P("O objetivo consiste na criação do dashboard contendo gráficos informativos sobre DSTs, com a finalidade de tornar simples o entendimento dos dados de forma acessível pelas pessoas interessadas sobre a doença, pois a maioria dos dados coletados não são apresentados em um formato estruturado, ocorrendo dificuldade nas interpretações das análises para quem os consulta."),
                           ], className="timeline_content"), 
                        ]),

                        html.Li([
                           html.Div([
                                html.Span(className="bi bi-wechat"),
                                html.H4("Propotipar"),
                                html.P("Mas se os dados estão disponíveis a todos porque muitas pessoas têm essa dificuldade? Em virtude do formato que os mesmos são disponibilizados. A maioria das tabelas de dados estão em formato CSV não manipulados, ou por API a banco de dados. Logo, pessoas fora da área tecnológica podem possuir limitações no acesso às informações."),
                           ], className="timeline_content"), 
                        ]),

                        html.Li([
                           html.Div([
                                html.Span(className="bi bi-bullseye"),
                                html.H4("Testar"),
                                html.P("E como é típico, a área da saúde no Brasil sempre carece de informações ao público, então vamos fazer nosso projeto aberto e útil a qualquer pessoa que precise fazer sua consulta."),
                           ], className="timeline_content"), 
                        ]),

                    ], className="timeline-list"),
                ], className="col-xl-12"),
            ], className="row"),

    ], className="experience pt-100 pb-100", id="experience"),

])