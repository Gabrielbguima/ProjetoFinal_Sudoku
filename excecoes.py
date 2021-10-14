from log import *

'''
Esse arquivo é um conjunto de métodos que colecionam erros específicos do meu jogo de sudoku.
'''

def CommandError():

    try:

        print('Comando inválido')
        log.addLog('CommandError')

    except FileNotFoundError:

        print('Comando inválido')
        log()
        log.addLog('CommandError')
        log.addLog(FileNotFoundError)

def InvalidInput():

    try:

        print('Não é possível realizar esta ação')
        log.addLog('InvalidInput')

    except FileNotFoundError:

        print('Não é possível realizar esta ação')
        log()
        log.addLog('InvalidInput')
        log.addLog(FileNotFoundError)

def ImpossivelCarregar():

    try:

        print('Nenhuma partida registrada. Você deve jogar primeiro.')
        log.addLog('ImpossivelCarregar')

    except FileNotFoundError:

        print('Nenhuma partida registrada. Você deve jogar primeiro.')
        log.addLog('ImpossivelCarregar')
        log.addLog(FileNotFoundError)
    
