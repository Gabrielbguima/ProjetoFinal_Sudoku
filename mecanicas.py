from excecoes import *
from validSudoku import *
from excecoes import *
from msvcrt import getch
from loadsave import *
from log import *

class Mecanicas:

    comandos_permitidos = {'1','2','3','4','5','6','7','8','9'} #ainda será complementado
    atributos = {'comando', 'comandos'}
    metodos = {'tempo', 'qntErros', 'teclas','getAtributos', 'getMetodos', 'getManual'}

    def teclas(self, comando, comandos = comandos_permitidos):
        '''
        Usando o getch será definidas as teclas que podem ser usadas no jogo, caso não esteja dentro das teclas
        autorizadas, será retornada uma mensagem de erro.
        '''
        try:

            if comando in comandos:
                return True

            else:
                raise CommandError

        except:
            CommandError

        
    
    def tempo(self):    #da uma dica resposta aleatória dentro do tabuleiro, terá máximo de uso.
        pass
    
    def qntErros(self):
        pass
    
    def ganhou(self): 
        '''
        Exibe uma mensagem de parabenização caso o jogador tenha completado o tabuleiro, mostra a qunatidade de 
        erros e tempo.
        '''
        pass

    def errou(self):
        '''
        Essa função tem o intuito de verificar se o jogador errou, comparando o tabuleiro solução com o tabuleiro
        que ele está preenchendo. toda vez que o jogador errar será contabilizado. Quando o jogador errar 3 vezes
        será exibida uma mensagem de derrota. Perguntando se ele quer jogar outra ou voltar ao menu principal.
        '''
        pass
    
    def jogada(self, num, pos): 
        '''
        recebe um numero do 1 a 9, a função verificará se trata de um numero dentro dos paramentros do jogo
        e realizará a efetivação da jogada na posição selecionada
        '''        
        pass
    
    def apagarjogada(self, pos): 
        '''
        Pega uma posição do tabuleiro e o remove o seu numero
        tomar cuidado para não apagar uma posição que já é nativa do tabuleiro. Ou seja, pré configurada
        Qunado isso acontecer retornar uma mensagem de erro
        '''
        pass

    def dicas(self):
        '''
        Tem a função de dar dicas ao jogador sobre o tabuleiro, serão 3 dicas possíveis. Toda vez que é pedido
        dica aleatóriamente é escolhida uma casa para ser revelada.
        '''
        pass


    def getAtributos(self, atributos = atributos):
        return atributos
    
    def getMetodos(self, metodos = metodos):
        return metodos
    
    def getManual(self):
        pass
    
#movimento do jogador no tabuleiro
#números permitidos
#mensagem de erro
#casas erradas
#apagar (posso colocar voltar, usando o arquivo que armazena todas as jogadas)
#dicas
#sair
#desistir

#FAZER A GETMETODOS E GETATRIBUTOS