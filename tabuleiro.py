from validSudoku import *
from log import *
import numpy as np

class Tabuleiro:
    '''
    A classe tabuleiro foi criada para lidar com coisas relacionadas ao tabuleiro do sudoku.
    Preencher tabuleiro, preparar para jogar e etc.
    '''

    def __init__(self, tabuleiro = None): #receberá o formato do tabuleiro e os números permitidos nele 
        
        if tabuleiro == None:

            tabuleiro = getSudoku()
            self.tabuleiro = np.array(tabuleiro)
            print(self.tabuleiro)
            print_board(self.tabuleiro)

        
    def preparar(self):  #irá apagar os numeros de forma que seja possivel resolver o tabuleiro
        '''
        A função foi criada para preparar um tabuleiro de sudoku colocando 0 em partes aleatórias do tabuleiro
        com uma certa quantidade para que seja possível a resolução do puzzle.
        '''
        tabuleiro = self.tabuleiro
        print(tabuleiro)
        i = 0

        while i < 30:

            linha = random.randrange(1,9)
            coluna = random.randrange(1,9)

            if tabuleiro[linha][coluna] != 0:

                tabuleiro[linha][coluna] = 0
                i += 1
        
        return tabuleiro

    def terminou(self, tabuleiro):
        '''
        Função criada para verificar se o jogador terminou o tabuleiro, caso ele tenha terminado é retornado True
        caso ainda não tenha terminado é retornado False. Isso foi feito para a mensagem de 'conclui' do jogo.
        O usuario quando terminar de jogar pode clicar em concluir, caso o jogador não tenha preenchido o tabuleiro
        todo é exibida a mensagem:
        'Voce não preecheu todo o tabuleiro! Deseja desistir?'

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


t1 = Tabuleiro()
tp = Tabuleiro.preparar(t1)
print_board(tp)

#FAZER A GETMETODOS E A GETATRIBUTOS