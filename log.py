class log():
    '''
        Classe tem como objetivo armazenar exceções no código do Sudoku mesmo que estejam sendo corrigidas.
    '''
    def __init__(self, arqlog = None):

        if arqlog == None:

            self.arqlog = open('log.txt', 'w')
            self.arqlog.close()

        else:

            self.arqlog = open(arqlog, 'r')
            self.arqlog.close()

#Erros que podem ter dentro do Sudoku
#Entrada de teclas erradas dentro do jogo; uma entrada que não seja de 1 a 9
#Tentar remover um número que seja do tabuleiro base do jogo
#Erro de dicas além do esperado
#colocar um número em um espaço do tabuleiro já ocupado


#FAZER A GETMETODOS E A GETATRIBUTOS
