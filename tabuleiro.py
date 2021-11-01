from validSudoku import *
from log import *
import numpy as np
from copy import deepcopy

class Tabuleiro:
    '''
    A classe tabuleiro foi criada para lidar com coisas relacionadas ao tabuleiro do sudoku.
    Preencher tabuleiro, preparar para jogar e etc.
    '''
    metodos = {'__init__','preparar','tabuleiroResolvido','terminar', 'getAtributos', 'getMetodos', 'getManual'}
    atributos = {'tabuleiro'}

    def __init__(self, tabuleiro = None): #receberá o formato do tabuleiro e os números permitidos nele 
        
        if tabuleiro == None:

            tabuleiro = getSudoku()
            self.tabuleiro = tabuleiro
            self.tabuleiro2 = deepcopy(tabuleiro)

        
    def preparar(self):  #irá apagar os numeros de forma que seja possivel resolver o tabuleiro
        '''
        A função foi criada para preparar um tabuleiro de sudoku colocando 0 em partes aleatórias do tabuleiro
        com uma certa quantidade para que seja possível a resolução do puzzle.
        '''
        tabuleiro = self.tabuleiro
        i = 0

        while i < 30:

            linha = random.randrange(1,9)
            coluna = random.randrange(1,9)

            if tabuleiro[linha][coluna] != 0:

                tabuleiro[linha][coluna] = 0
                i += 1
        
        return tabuleiro
    
    def tabuleiroResolvido(self):
        '''
        Função criada a para armazenar o tabuleiro resolvido, uma cópia, e ser usado pra comparar com o tabuleiro
        do usuário posteriormente. 
        '''

        tabuleiro2 = self.tabuleiro2

        try:
            tabuleiro_resolvido = open('tabuleiroResolvido.txt', 'w')

            for i in range(len(self.tabuleiro2)):
                
                tabuleiro_resolvido.write(f'{str(self.tabuleiro2[i])}\n')

            tabuleiro_resolvido.close()

            return tabuleiro2

        except FileNotFoundError:
            print('O arquivo não foi encontrado')
            log.addLog('FileNotFoundError')

    def terminou(tabuleiro):
        '''
        Função criada para verificar se o jogador terminou o tabuleiro, caso ele tenha terminado é retornado True
        caso ainda não tenha terminado é retornado False. Isso foi feito para a mensagem de 'conclui' do jogo.

        Caso contrário, com a função retornando True.
        Entra a averiguação de erros, se ele conseguiu ganhar e é printado o tempo dele.
        '''
        vazio = 0

        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro[0])):
                if tabuleiro[i][j] == 0:
                    vazio += 1

        if vazio == 0:
            return True

        else:
            return False

    def getAtributos(self, atributos = atributos):
        return atributos
    
    def getMetodos(self, metodos = metodos):
        return metodos
    
    def getManual(self):
        """
            Esta função estática (chamada sempre através de Tela.getManual()) retorna um 
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        metodos = {'__init__','preparar','tabuleiroResolvido','terminou', 'getAtributos', 'getMetodos', 'getManual'}
        atributos = {'tabuleiro'}
        """
        manual = {}
        manual['__init__']              = Tabuleiro.__init__.__doc__
        manual['preparar']              = Tabuleiro.preparar.__doc__
        manual['tabuleiroResolvido']    = Tabuleiro.tabuleiroResolvido.__doc__
        manual['terminou']              = Tabuleiro.terminou.__doc__
        manual['getAtributos']          = Tabuleiro.getAtributos.__doc__
        manual['getMetodos']            = Tabuleiro.getMetodos.__doc__
        manual['getManual']             = Tabuleiro.getManual.__doc_
                
        return manual
#FAZER A GETMETODOS E A GETATRIBUTOS