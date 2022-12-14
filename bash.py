import os

def executeCmd(comand):
    f = os.popen(f'{comand}')
    output = f.read()
    return output

