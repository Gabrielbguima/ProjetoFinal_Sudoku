from typing import Type
from excecoes import *
from validSudoku import *
from excecoes import *
from msvcrt import getch
from loadsave import *
from log import *
from time import *

class Mecanicas:

    comandos_permitidos = {1, 2, 3, 4, 5, 6, 7, 8, 9}
                        
    atributos = {'comando', 'comandos'}
    metodos = {'errou','tabuleiroOriginal','jogada','apagarjogada','dicas', 'teclas','getAtributos', 'getMetodos', 'getManual'}

    def teclas(comando, comandos = comandos_permitidos):
        '''
        Usando o getch será definidas as teclas que podem ser usadas no jogo, caso não esteja dentro das teclas
        autorizadas, será retornada uma mensagem de erro.
        '''

        try:

            if comando in comandos:
                comando = int(comando)
                return comando

            else:
                raise CommandError

        except:
            CommandError
    
    def errou(tabuleiro, board, qnt_erros = 0):
        '''
        Essa função tem o intuito de verificar se o jogador errou, comparando o tabuleiro solução com o tabuleiro
        que ele está preenchendo. toda vez que o jogador errar será contabilizado. Quando o jogador errar 3 vezes
        será exibida uma mensagem de derrota. Perguntando se ele quer jogar outra ou voltar ao menu principal.
        '''
        numeros = {'0':0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}
        erros = qnt_erros

        lista = [[],[],[],[],[],[],[],[],[]]
        verificar = open('tabuleiroAtual.txt','r')
        leitura = verificar.readlines()

        for i in range(len(leitura)):
            for j in range(len(leitura[i])):

                if leitura[i][j] in numeros:
                    aux = numeros[leitura[i][j]]
                    lista[i].append(aux)

        if erros <= 10:

            for i in range(len(lista)):
                for j in range(len(lista[i])):
                    if lista[i][j] > 0:
                        if board[i][j] != lista[i][j]:
                            erros += 1
            if erros == qnt_erros:

                return erros

            else:
                print('Você errou!')
                return erros

        else:
            print('Você perdeu :(')
            return erros
                
    def tabuleiroOriginal(tabuleiro):
        '''
        Essa função marca o tabueleiro não resolvido assim que ele é preparado. Criado especialmente para lidar
        com a função apagarJogada impedindo que o jogador reescreva o tabuleiro original apagando células primárias
        do puzzle. A função deve ser chamada assim que se inicia um novo jogo.
        '''
        try:

            fixas = open('tabuleiroOriginal.txt', 'w')

            for i in range(len(tabuleiro)):

                fixas.write(f'{str(tabuleiro[i])}\n')

            fixas.close()

        except FileNotFoundError:

            print('Erro, arquivo não encontrado')
            log.addLog('FileNotFoundError')
        

    def jogada(num, pos, tabuleiro): 
        '''
        recebe um numero do 1 a 9, a função verificará se trata de um numero dentro dos paramentros do jogo
        e realizará a efetivação da jogada na posição selecionada
        ''' 

        if len(pos) != 2:

            print('Devem ser dois números um para linha outra pra coluna')
        
        else:

            comando = Mecanicas.teclas(num)
            linha, coluna = pos[0], pos[1]

            if tabuleiro[linha - 1][coluna - 1] == 0:

                tabuleiro[linha - 1][coluna - 1] = comando
                return tabuleiro

            else:
                try:
                    print('A célula deve estar vazia; preenchida com 0')
                    log.addLog('InvalidInput')
                    return tabuleiro

                except TypeError:
                    log.addLog('TypeError')
                    pass

    
    def apagarjogada(pos, tabuleiro): 
        '''
        Pega uma posição do tabuleiro e o remove o seu numero
        tomar cuidado para não apagar uma posição que já é nativa do tabuleiro. Ou seja, pré configurada
        Qunado isso acontecer retornar uma mensagem de erro
        '''

        numeros = {'0':0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}

        if len(pos) != 2:

            print('Devem ser dois números um para linha outra pra coluna')
        
        else:

            linha, coluna = pos[0] - 1, pos[1] - 1

            try:
                #método que usei para transforamar o txt em uma matriz novamente
                lista = [[],[],[],[],[],[],[],[],[]]
                verificar = open('tabuleiroOriginal.txt','r')
                leitura = verificar.readlines()

                for i in range(len(leitura)):
                    for j in range(len(leitura[i])):
    
                        if leitura[i][j] in numeros:
                            aux = numeros[leitura[i][j]]
                            lista[i].append(aux)

                if lista[linha][coluna] > 0: 

                #se o número do tabuleiro da lista que é o primeiro tabuleiro for diferente retorna uma mensagem
                #de erro              

                    print('Não é possível reescrever uma célula original!')

                    log.addLog('InvalidInput')

                    return tabuleiro

                else:

                    tabuleiro[linha][coluna] = 0

                    return tabuleiro

            except FileNotFoundError:

                print('Arquivo não encontrado')
                log.addLog('FileNotFoundError')

    def dicas(tabuleiro, solucao, dicas_usadas = 0):
        '''
        Tem a função de dar dicas ao jogador sobre o tabuleiro, serão 3 dicas possíveis. Toda vez que é pedido
        dica aleatóriamente é escolhida uma casa para ser revelada.
        '''
        dicas_usadas = dicas_usadas + 1

        if dicas_usadas <= 3:

            while True:
                
                linha = random.randrange(1,9)
                coluna = random.randrange(1,9)

                if tabuleiro[linha][coluna] == 0:
                    
                    num = solucao[linha][coluna]
                    
                    print(f'Sua dica foi:{solucao[linha][coluna]} na posição {linha + 1, coluna + 1} ')

                    return num, linha + 1, coluna + 1, dicas_usadas

        else:

            print('Você não possui mais dicas :(')


    def getAtributos(self, atributos = atributos):
        return atributos
    
    def getMetodos(self, metodos = metodos):
        return metodos
    
    def getManual(self):
        """
            Esta função estática (chamada sempre através de Tela.getManual()) retorna um 
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        """
        manual = {}
        manual['errou']                 = Mecanicas.errou.__doc__
        manual['tabuleiroOriginal']     = Mecanicas.tabuleiroOriginal.__doc__
        manual['jogada']                = Mecanicas.jogada.__doc__
        manual['apagarjogada']          = Mecanicas.apagarjogada.__doc__
        manual['dicas']                 = Mecanicas.dicas.__doc__
        manual['teclas']                = Mecanicas.teclas.__doc__
        manual['getAtributos']          = Mecanicas.getAtributos.__doc__
        manual['getMetodos']            = Mecanicas.getMetodos.__doc__
        manual['getManual']             = Mecanicas.getManual.__doc_
                
        return manual
    