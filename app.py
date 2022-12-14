from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import data_table as dta
import terminal
import bash
import dash_bootstrap_components as dbc
import hardware
import filesystem

external_stylesheets = external_stylesheets=[dbc.themes.BOOTSTRAP]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Interval(
        id="refresh-interval",
        disabled=False,
        interval=2000,
        max_intervals=-1,
        n_intervals=0
    ),

    html.H1('Dashboard do computador - Sistemas Operacionais', style={"text-align":"center"}),

    html.P(children='''
    Projeto da disciplina de sistemas operacionais que visa a criação de um 
    dashboard para mostrar as principais informações do computador.
    ''', style={"text-align":"center"}),

    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Processos', value='tab-1'),
        dcc.Tab(label='Hardware', value='tab-2'),
        dcc.Tab(label='Sistema de arquivos', value='tab-3'),
        dcc.Tab(label='Terminal', value='tab-4'),
    ]),

    dcc.RadioItems(
        options=[
            {'label': 'Atualizar', 'value': 'False'},
            {'label': 'Parar', 'value': 'True'},
        ],
        value='False',
        id='radiobtn',
        style={"display":"flex", "justify-content":"space-evenly", "margin-top":"10px"}
    ),

    html.Button(id='submit-val', style={"display":"none"}),
    html.Button(id='cmd-output', style={"display":"none"}),
    html.Button(id='input', style={"display":"none"}),

    html.Div(id='tab-content')
])

# CALLBACKS
@app.callback(Output('tab-content', 'children'),
              Input('tabs', 'value'),
              Input('refresh-interval','n_intervals'))
def render_content(tab, n):
    if tab == 'tab-1':       
        return dta.getDataTable()
    elif tab == 'tab-2':        
        return hardware.getHardware()
    elif tab == 'tab-3':
        return filesystem.getDiskTable()
    elif tab == 'tab-4':
        return terminal.openTerminal()


@app.callback(Output('refresh-interval', 'disabled'),
              Input('radiobtn', 'value'),
)
def pauseInterval(value):
    if value == "True": return True 
    else: return False


# CALLBACK DO TERMINAL
@app.callback(
    Output("cmd-output", "value"),
    Input("submit-val", "n_clicks"),
    State("input", "value"),
    prevent_initial_call=True
)
def update_output(n_clicks, value):
    return bash.executeCmd(value)

if __name__ == '__main__':
    app.run_server(debug=True)