#POR ALGUM MOTIVO AS CLASSES ESTÃO SENDO ATIVADAS QUANDO SE INICIA O JOGO
from log import *

def CommandError():

    try:

        print('Comando inválido')
        addLog(CommandError)

    except FileNotFoundError:

        print('Comando inválido')
        log()
        addLog(CommandError)
        addLog(FileNotFoundError)

def InvalidInput():

    try:

        print('Não é possível realizar esta ação')
        addLog(InvalidInput)

    except FileNotFoundError:

        print('Não é possível realizar esta ação')
        log()
        addLog(InvalidInput)
        addLog(FileNotFoundError)

def ImpossivelCarregar():

    try:

        print('Nenhuma partida registrada. Você deve jogar primeiro.')
        addLog(ImpossivelCarregar)

    except FileNotFoundError:

        print('Nenhuma partida registrada. Você deve jogar primeiro.')
        addLog(ImpossivelCarregar)
        addLog(FileNotFoundError)
    
