import pandas as pd
import os

def getTop():

    # Executa o comando top e salva a saída num arquivo pivo.csv
    top_command = "top -b -n 1 | sed -n '7, ${s/^ *//;s/ *$//;s/  */;/gp;};$q' > pivo.csv"
    os.system(top_command)

    # Através do arquivo pivo.csv, substituo as ',' por '.'
    replace_command = "sed 's/,/\./g' pivo.csv > top-output.csv"
    os.system(replace_command)

    # Deleta o arquivo pivo
    os.system("rm pivo.csv")

    # Transforma o arquivo csv em um data frama pandas
    df = pd.read_csv("top-output.csv", sep=";", on_bad_lines='skip')

    return df
