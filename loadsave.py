#Essa classe tem como função armazenar os dados referentes ao hitórico de jogadas do jogador, tempo,
# quantidade de erros e acertos, podendo salvar para montar estatísticas e salvar o progresso
from jogador import *
from validSudoku import *
from log import *

class loadSave():
    '''
    Essa classe tem como o objetivo criar um arquivo .txt que armazena jogadas, nome do jogador, erros,
    se ganhou, perdeu ou desistiu. Além de recarregar o arquivo caso necessário.
    '''
    def __init__(self, arquivo = None):

        if arquivo == None:

            self.arquivo = open('historico.txt', 'w')
            self.arquivo.write(self.nome)
            self.arquivo.close()
        
        else:

            self.arquivo = open(arquivo, 'r')
            self.arquivo.close()
    
    def salvarJogada(self, jogada, arquivo = 'historico.txt'):
        '''
            Adiciona ao arquivo criado a ultima jogada, recebendo como parâmetro
            a ultima jogada e o arquivo já criado.
            Deve ser utilizado na classe Sudoku para cada jogada realizada seja registrada.
            A jogada vai vir em forma de tupla, (x, i, j); x sendo o número jogado, i a linha da matriz
            j a coluna da matriz, o tabuleiro é uma matriz, i e j são coordenadas.

            tuple -> None
        '''
        try:

            adicionar = open(arquivo, 'a')
            adicionar.write(jogada)
            adicionar.close()

        except FileNotFoundError:

            arquivo = open('save.txt', 'w')
            arquivo.close()
            arquivo = open('save.txt', 'a')
            arquivo.write(jogada)
            log.addLog('FileNotFoundError')

    def salvarTabuleiro(self, board):
        '''
        Essa função tem como objetivo armazenar o tabuleiro do jogo que está sendo jogado e a cada nova jogada
        reescrevê-lo assim quando a função 'continuar'(continuar deve ser criada na sudoku) for executada 
        ele usará do arquivo criado nessa função para passar o tabuleiro para o jogador.

        Essa função corresponde ao item 5.3 da p2
        str -> None
        '''
        try:
            tabuleiro_atual = open('tabuleiroAtual.txt', 'w')
            arquivo = open(board, 'r')

            for i in arquivo:
                tabuleiro_atual.write(i)

            tabuleiro_atual.close()
            arquivo.close()

        except FileNotFoundError:
            print('O arquivo não foi encontrado')
            log.addLog('FileNotFoundError')

    def novoJogo(self, arquivo):
        '''
        Para cada novo jogo iniciado ele adiciona uma nova linha no arquivo que representa um novo jogo.
        Ele adiciona um \n ao final de do arquivo .txt fazendo que ele pule uma linha para escrever na outra linha
        as jogadas da próxima partida, isso ajuda posteriormente a usar o readlines para coletar informações
        para as estatísticas

        Essa função só funciona com o arquivo do primeiro jogo já carregado então deve-se jogar uma primeira vez
        '''
        try:

            adicionar = open(arquivo, 'a')
            adicionar.write('\n')
            adicionar.close()

            return True

        except  FileNotFoundError:

            print('Essa função só funciona com arquivo já criado, necessita jogar a primeira vez')
            log.addLog('FileNotFoundError')


#FAZER A GETMETODOS E A GETATRIBUTOS