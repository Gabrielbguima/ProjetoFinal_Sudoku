from validSudoku import *
from log import *

class Tabuleiro:

    def __init__(self, tabuleiro = None): #receberá o formato do tabuleiro e os números permitidos nele 
        
        if tabuleiro == None:

            self.tabuleiro = getSudoku()
            print_board(self.tabuleiro)

        
    def preparar(self, tabuleiro):  #irá apagar os numeros de forma que seja possivel resolver o tabuleiro
        pass

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


t1 = Tabuleiro

#FAZER A GETMETODOS E A GETATRIBUTOS