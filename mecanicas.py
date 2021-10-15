from excecoes import *
from validSudoku import *
from excecoes import *
from msvcrt import getch
from loadsave import *
from log import *
from time import *

class Mecanicas:

    comandos_permitidos = {'1','2','3','4','5','6','7','8','9'} #ainda será complementado
    atributos = {'comando', 'comandos'}
    metodos = {'tempo', 'qntErros', 'teclas','getAtributos', 'getMetodos', 'getManual'}

    def teclas(self, comando, comandos = comandos_permitidos):
        '''
        Usando o getch será definidas as teclas que podem ser usadas no jogo, caso não esteja dentro das teclas
        autorizadas, será retornada uma mensagem de erro.
        '''

        #pode ser que eu precise adaptar essa função para pegar o comando em getch e transformar no número inteiro

        try:

            if comando in comandos:
                return comandos[comando]

            else:
                raise CommandError

        except:
            CommandError

        
    
    def tempo(self):    #da uma dica resposta aleatória dentro do tabuleiro, terá máximo de uso.
        pass
    
    def ganhou(self, erros, tempo, dicas_usadas): 
        '''
        Exibe uma mensagem de parabenização caso o jogador tenha completado o tabuleiro, mostra a qunatidade de 
        erros e tempo.
        '''

        pass

    def errou(self, solucao, tabuleiroAtual):
        '''
        Essa função tem o intuito de verificar se o jogador errou, comparando o tabuleiro solução com o tabuleiro
        que ele está preenchendo. toda vez que o jogador errar será contabilizado. Quando o jogador errar 3 vezes
        será exibida uma mensagem de derrota. Perguntando se ele quer jogar outra ou voltar ao menu principal.
        '''
        erros = 0

        for i in range(len(tabuleiroAtual)):
            for j in range(len(tabuleiroAtual[0])):

                if solucao[i][j] != tabuleiroAtual[i][j]:

                    erros += 1
        
        return erros
                
    
    def jogada(self, num, pos, tabuleiro): 
        '''
        recebe um numero do 1 a 9, a função verificará se trata de um numero dentro dos paramentros do jogo
        e realizará a efetivação da jogada na posição selecionada
        ''' 

        if len(pos) != 2:

            print('Devem ser dois números um para linha outra pra coluna')
        
        else:

            comando = Mecanicas.teclas(num)
                
            linha, coluna = pos[0], pos[1]

            if tabuleiro[linha][coluna] == 0:

                tabuleiro[linha][coluna] = comando
                return tabuleiro

            else:
                print('A célula deve estar vazia; preenchida com 0')
    
    def apagarjogada(self, pos, tabuleiro): 
        '''
        Pega uma posição do tabuleiro e o remove o seu numero
        tomar cuidado para não apagar uma posição que já é nativa do tabuleiro. Ou seja, pré configurada
        Qunado isso acontecer retornar uma mensagem de erro
        '''
        #ver como vai ser para implementar a parte que ele não pode apagar 
        if len(pos) != 2:

            print('Devem ser dois números um para linha outra pra coluna')
        
        else:

            linha, coluna = pos[0], pos[1]
            tabuleiro[linha][coluna] = 0

            return tabuleiro

    def dicas(self, tabuleiro, solucao, dicas_usadas = 0):
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
                    
                    tabuleiro[linha][coluna] = solucao[linha][coluna]

                    return tabuleiro

        else:

            print('Você não possui mais dicas :(')


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