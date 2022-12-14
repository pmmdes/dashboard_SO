from dash import html
import dash_bootstrap_components as dbc
import pandas as pd
import psutil

partitions = psutil.disk_partitions()

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

def diskTable():
    disk_info = []

    partitions = psutil.disk_partitions()
    for p in partitions:
        
        try:
            p_usage = psutil.disk_usage(p.mountpoint)
        except PermissionError:
            # nao pode ser lido
            continue
    

        disk_info.append([p.device, p.mountpoint, p.fstype, get_size(p_usage.total), get_size(p_usage.used), get_size(p_usage.free), p_usage.percent])

    df = pd.DataFrame(disk_info)
    df.columns = ["Dispositivo", "Mount", "Sistema de Arquivos", "Espaço Total", "Usado", "Livre", "%"]

    return df

def getDiskTable():
    return html.Div(children=[

        html.H3(children="Sistemas de arquivos e Partições", style={"text-align": "center", "padding":"25px"}),

        html.Div(children=[
            dbc.Table.from_dataframe(diskTable(), striped=True, bordered=True, hover=True, color="dark", style={"width": "80%"})
        ], style={"display":"flex","justify-content": "center"} ), 

    ])