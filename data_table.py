from dash import html, dash_table, dcc
import read_top as top
import plotly.graph_objects as go

def getDataTable():

    df = top.getTop()

    # cria dataframe de stats, funcionando como pivo
    statsdf = df
    statsdf.convert_dtypes()

    # cria dataframe ordenado pelo consumo de CPU
    cpudf = statsdf.sort_values(by=['%CPU'],ascending=False).head(10)

    # cria gráfico do consumo de CPU
    cpufig = go.Figure(
        data=[go.Bar(x=cpudf['COMANDO'], y=cpudf['%CPU'])],
        layout=go.Layout(
                    title=go.layout.Title(text="Consumo de CPU por processo (10 primeiros)")
        )
    )
    # cria gráfico do consumo de memória
    memfig = go.Figure(
        data=[go.Bar(x=cpudf['COMANDO'], y=cpudf['%MEM'])],
        layout=go.Layout(
                    title=go.layout.Title(text="Consumo de memória por processo (10 primeiros)")
        )
    )

    return html.Div(children=[

    html.H1(children='Tabela de saída do comando top', style={'margin-top':20, "text-align":"center"}),

    html.P(children='A saída do comando top é tabelada, com paginação e possibilidade de ordenar por colunas.', style={"text-align":"center"}),

    dash_table.DataTable(
    df.to_dict('records'), 
    page_size=10,
    style_table={"padding":"15px"},
    style_cell={'textAlign': 'center'},
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(220, 220, 220)',
        }
    ],
    style_header={
        'backgroundColor': 'rgb(30, 30, 30)',
        'color': 'white'
    },
    sort_action="native",
    sort_mode="multi",
    ),

    dcc.Graph(
        figure=cpufig
    ),

    dcc.Graph(
        figure=memfig
    ),

])
