#Essa classe tem como função armazenar os dados referentes ao hitórico de jogadas do jogador, tempo,
# quantidade de erros e acertos, podendo salvar para montar estatísticas e salvar o progresso
from jogador import *
from validSudoku import *

class loadSave():
    '''
    Essa classe tem como o objetivo criar um arquivo .txt que armazena jogadas, nome do jogador, erros,
    se ganhou, perdeu ou desistiu. Além de recarregar o arquivo caso necessário.
    '''
    def __init__(self, arquivo = None):

        if arquivo == None:

            self.arquivo = open('save.txt', 'w')
            self.arquivo.close()
        
        else:

            self.arquivo = open(arquivo, 'r')
            self.arquivo.close()
    
    def salvarjogada(self, jogada, arquivo):
        '''
            Adiciona ao arquivo criado a ultima jogada, recebendo como parâmetro
            a ultima jogada e o arquivo já criado.
            Deve ser utilizado na classe Sudoku para cada jogada realizada seja registrada.
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

        except ValueError:

            if jogada is not str:

                print('Error, valor inválido')
    
    '''
        PROCURAR SABER SE É MELHOR FAZER O MÉTODO QUE ESCREVE UMA NOVA LINHA PARA UM NOVO JOGO É MELHOR
        NESSA PARTE DO CÓDIGO OU EM OUTRA
    '''
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

    def carregar(self, arquivo):#TESTAR FUNÇÃO CARREGAR
        '''
        Essa classe se encarregará de dar o recarregamento da última partida parada do jogador.
        Ela abre o arquivo save que contém o último tabuleiro criado. Após isso, cria-se uma variavel com 
        um tabuleiro vazio, a partir disso usa-se a função find_empty da validSudoku para achar os espaços
        vazios e retornar uma lista. Se não está vazio ele retorna True, porém caso esteja vazio as variáveis
        linha e coluna recebema variável achar e usamos um loop para cada ir assumindo cada linha do arquivo
        save.txt nos readlines com a quantidade de linhas e colunas vazias, nisso o board vazio vai sendo preenchido
        pelos dados do arquivo, fecha-se o arquivo e retorna-se o board dessa vez preechido.
        '''
        try:
            save = open(arquivo, 'r')
            board = [
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]
            ]

            achar = find_empty(board)

            if not achar:

                return True

            else:

                linha,coluna = achar
            
            for i in save.readlines[linha][coluna]:

                board[linha][coluna] = i

            save.close()

            return board

        except  FileNotFoundError:

            print('Infelizmente é impossível carregar o jogo, pois o arquivo não existe')

#FAZER A GETMETODOS E A GETATRIBUTOS