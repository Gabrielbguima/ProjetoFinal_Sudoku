#POR ALGUM MOTIVO AS CLASSES ESTÃO SENDO ATIVADAS QUANDO SE INICIA O JOGO

class CommandError():

    try:

        print('Comando inválido')
        log = open('log.txt', 'a')
        log.write(f'CommandError\n')
        log.close()

    except FileNotFoundError:

        print('Comando inválido')
        log = open('log.txt', 'w')
        log.write('CommandError\n')
        log.close()

class InvalidInput():

    try:

        print('Não é possível realizar esta ação')
        log = open('log.txt', 'a')
        log.write(f'InvalidInput\n')
        log.close()

    except FileNotFoundError:

        print('Não é possível realizar esta ação')
        log = open('log.txt', 'w')
        log.write(f'InvalidInput\n')
        log.close()

class ImpossivelCarregar():

    try:

        print('Nenhuma partida registrada. Você deve jogar primeiro.')
        log = open('log.txt', 'a')
        log.write(f'ImpossivelCarregar\n')
        log.close()

    except FileNotFoundError:

        print('Nenhuma partida registrada. Você deve jogar primeiro.')
        log = open('log.txt', 'w')
        log.write(f'ImpossivelCarregar\n')
        log.close()
    
