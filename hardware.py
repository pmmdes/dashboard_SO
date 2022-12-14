import psutil
import platform
from dash import html
import dash_bootstrap_components as dbc

def verifyColor(number):
    if number < 25.0:
        return "success"
    elif number >= 25.0 and number < 50.0:
        return "warning"
    else:
        return "danger"



#############################
# Sistema
uname = platform.uname()
system_info = uname.system
node_info = uname.node
release_info = uname.release
version_info = uname.version
machine_info = uname.machine
processor_info = uname.processor

# Memória


#####################################

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def getHardware():

    # Uso de CPU por núcleo
    cpuusage = []
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        color = verifyColor(percentage)
        cpuusage.append([i, percentage, color])
    cputotal = psutil.cpu_percent()
    
    svmem = psutil.virtual_memory()
    swap = psutil.swap_memory()

    return html.Div(children=[

        
        html.Div(children=[

            # PARTE DO SISTEMA
            html.Div(children=[
                html.H3(children="Informações do sistema", style={"text-align": "center","padding":"15px"}),

                html.Div(children=[
                    html.Div(children=[
                        html.P(children=f"SISTEMA: {system_info}"),
                        html.P(children=f"NODE: {node_info}"),
                        html.P(children=f"RELEASE: {release_info}"),
                    ], style={"text-align":"left"}),
                    html.Div(children=[
                        html.P(children=f"VERSÃO: {version_info[:14]}"),
                        html.P(children=f"MÁQUINA: {machine_info}"),
                        html.P(children=f"PROCESSADOR: {processor_info}"),
                    ], style={"text-align":"left"}),
                ], style={"display": "flex", "justify-content": "space-evenly", "margin-top":"50px"}),
            ], style={"width":"50%"}),

            html.Div(style={"height":"250px", "width": "0px", "border":"solid 1px #c0c0c0","margin-top":"30px" }),

            # PARTE DO CPU
            html.Div(children=[
                html.H3(children="Uso de CPU", style={"text-align": "center", "padding":"15px 15px 5px 15px"}),

                html.P(children=f"Consumo de cada core de CPU em %", style={"text-align": "center"}), 

                html.Div(children=[

                    html.Div(children=[
                        html.P(children=f"Core #0 ", style={"margin-right":"10px"}),
                        dbc.Progress(value=cpuusage[0][1], label=f"{cpuusage[0][1]}%", style={"height": "30px", "width":"50%"}, color=cpuusage[0][2]),
                        html.P(children=f" ({cpuusage[0][1]}%)"),
                    ], style={"display": "flex"}),

                    html.Div(children=[
                        html.P(children=f"Core #1 ", style={"margin-right":"10px"}),
                        dbc.Progress(value=cpuusage[1][1], label=f"{cpuusage[1][1]}%", style={"height": "30px", "width":"50%"}, color=cpuusage[1][2]),
                        html.P(children=f" ({cpuusage[1][1]}%)"),
                    ], style={"display": "flex"}),

                    html.Div(children=[
                        html.P(children=f"Core #2 ", style={"margin-right":"10px"}),
                        dbc.Progress(value=cpuusage[2][1], label=f"{cpuusage[2][1]}%", style={"height": "30px", "width":"50%"}, color=cpuusage[2][2]),
                        html.P(children=f" ({cpuusage[2][1]}%)"),
                    ], style={"display": "flex"}),

                    html.Div(children=[
                        html.P(children=f"Core #3 ", style={"margin-right":"10px"}),
                        dbc.Progress(value=cpuusage[3][1], label=f"{cpuusage[3][1]}%", style={"height": "30px", "width":"50%"}, color=cpuusage[3][2]),
                        html.P(children=f" ({cpuusage[3][1]}%)"),
                    ], style={"display": "flex"}),
                ], style={"width":"100%", "margin-left": "130px"}),

                html.P(children=f"Consumo total de CPU em %", style={"text-align": "center"}),

                html.Div(children=[
                        html.P(children=f"Total: ", style={"margin-right":"10px"}),
                        dbc.Progress(value=cputotal, label=f"{cputotal}%", style={"height": "30px", "width":"50%"}, color=verifyColor(cputotal)),
                        html.P(children=f" ({cputotal}%)"),
                ], style={"display": "flex", "width":"100%", "margin-left": "150px"}),

            ], style={"width":"50%"}),

        ], style={"display": "flex", "justify-content":"space-evenly"}),


        html.Hr(),

        # PARTE DA MEMORIA

        html.H3(children="Uso de Memória", style={"text-align": "center"}),

        html.Div(children=[

            html.Div(children=[
                html.H3(children="Memória Principal"),
                html.P(children=f"Total: {get_size(svmem.total)}"),
                html.P(children=f"Disponível: {get_size(svmem.available)}"),
                html.P(children=f"Usado: {get_size(svmem.used)}"),
                html.P(children=f"Porcentagem: {svmem.percent}%"),
                dbc.Progress(value=svmem.percent, label=f"{svmem.percent}%", style={"height": "30px", "width":"50%", "margin-left": "180px"}, color=verifyColor(svmem.percent)),
            ], style={"text-align": "center", "width": "100%"}),

            html.Div(style={"height":"250px", "width": "0px", "border":"solid 1px #c0c0c0" }),

            html.Div(children=[
                html.H3(children="Memória SWAP"),
                html.P(children=f"Total: {get_size(swap.total)}"),
                html.P(children=f"Disponível: {get_size(swap.free)}"),
                html.P(children=f"Usado: {get_size(swap.used)}"),
                html.P(children=f"Porcentagem: {swap.percent}%"),
                dbc.Progress(value=swap.percent, label=f"{swap.percent}%", style={"height": "30px", "width":"50%", "margin-left": "180px"}, color=verifyColor(swap.percent)),
            ], style={"text-align": "center", "width": "100%"}),

        ], style={"display":"flex", "justify-content": "space-evenly"}),
        
        

    ])
