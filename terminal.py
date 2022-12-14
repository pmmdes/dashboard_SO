from dash import dcc, html

def openTerminal():
    return html.Div(children=[
        html.H1('Terminal de comandos', style={"text-align": "center", "padding-top":"15px"}),

        html.P(children='''
        Simulador de um terminal que processa comandos bash.
        ''', style={"text-align": "center"}),        

        html.Div(children=[
            html.Div(children=[
                html.H3('Entrada de comandos'),

                dcc.Input(id="input", type="text", placeholder="Digite um comando"),
            
                html.Button('Enviar', id='submit-val', n_clicks=0, style={'margin-left': 10}),
            ], style={"padding-left":"15px"}),
            
            html.Div(children=[
                html.H3('Saída de comandos'),

                dcc.Textarea(id="cmd-output", style={'width': '80%','height': 300} )
            ], style={"width":"70%", "margin-left":"20px"}),
        ], style={"display":"flex", "justify-content":"space-evenly"}),
])

