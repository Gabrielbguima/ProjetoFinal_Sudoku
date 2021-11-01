from tabuleiro import Tabuleiro
from validSudoku import *
from log import *

class loadSave():
    '''
    Essa classe tem como o objetivo criar um arquivo .txt que armazena jogadas, nome do jogador, erros,
    se ganhou, perdeu ou desistiu. Além de recarregar o arquivo caso necessário.
    '''
    metodos = {'__init__','salvarJogada','salvarTabuleiro','salvarResolucao', 'getAtributos', 'getMetodos', 'getManual'}
    atributos = {'arquivo'}

    def __init__(self, arquivo = None):

        if arquivo == None:

            self.arquivo = open('historico.txt', 'w')
            self.arquivo.close()
        
        else:

            try:
                self.arquivo = open(arquivo, 'r')
                self.arquivo.close()

            except FileNotFoundError:

                log.addLog('FileNotFoundError')
                self.arquivo = open('historico.txt', 'w')
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
            adicionar.write(jogada + ' ')
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

            for i in range(len(board)):
                
                tabuleiro_atual.write(f'{str(board[i])}\n')

            tabuleiro_atual.close()

        except FileNotFoundError:
            log.addLog('FileNotFoundError')

            tabuleiro_atual = open('tabuleiroAtual.txt', 'w')

            for i in range(len(board)):
                
                tabuleiro_atual.write(f'{str(board[i])}\n')

            tabuleiro_atual.close()

    def salvarResolucao(self, board):
        '''
        Essa função tem o objetivo de salvar a resolução do tabuleiro que foi colocado para ser jogado
        ele vai ser sobreescrito toda vez que tiver um novo jogo. Feito para rodar a parte do continuar com 
        todas as funções do Novo Jogo.
        '''
        try:

            tabuleiro_atual = open('tabuleiroResolvido.txt', 'w')

            for i in range(len(board)):
                
                tabuleiro_atual.write(f'{str(board[i])}\n')

            tabuleiro_atual.close()

        except FileNotFoundError:

            log.addLog('FileNotFoundError')
            tabuleiro_atual = open('tabuleiroResolvido.txt', 'w')

            for i in range(len(board)):
                
                tabuleiro_atual.write(f'{str(board[i])}\n')

            tabuleiro_atual.close()
            
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

    def getAtributos(self, atributos = atributos):
        return atributos
    
    def getMetodos(self, metodos = metodos):
        return metodos
    
    def getManual(self):
        """
            Esta função estática (chamada sempre através de Tela.getManual()) retorna um 
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        metodos = {'__init__','salvarJogada','salvarTabuleiro','salvarResolucao', 'getAtributos', 'getMetodos', 'getManual'}
        atributos = {'arquivo'}
        """
        manual = {}
        manual['__init__']              = loadSave.__init__.__doc__
        manual['salvarJogada']          = loadSave.salvarJogada.__doc__
        manual['salvarTabuleiro']       = loadSave.salvarTabuleiro.__doc__
        manual['salvarResolucao']       = loadSave.salvarResolucao.__doc__
        manual['getAtributos']          = loadSave.getAtributos.__doc__
        manual['getMetodos']            = loadSave.getMetodos.__doc__
        manual['getManual']             = loadSave.getManual.__doc_
                
        return manual
#FAZER A GETMETODOS E A GETATRIBUTOS