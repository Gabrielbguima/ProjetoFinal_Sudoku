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

    def armazenarErro(self, erro, arqlog):
        '''
        Tem como objetivo armazenar os erros em um arquivo
        '''
        erro_str = str(erro)
        log_txt = open(arqlog, 'a')
        log_txt.write(erro_str)
        log_txt.close()



#Erros que podem ter dentro do Sudoku
#Entrada de teclas erradas dentro do jogo; uma entrada que não seja de 1 a 9
#Tentar remover um número que seja do tabuleiro base do jogo
#Erro de dicas além do esperado
#colocar um número em um espaço do tabuleiro já ocupado


#FAZER A GETMETODOS E A GETATRIBUTOS
