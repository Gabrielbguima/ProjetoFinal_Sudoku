from validSudoku import *

class Tabuleiro:

    def __init__(self, tabuleiro = None): #receberá o formato do tabuleiro e os números permitidos nele 
        
        if tabuleiro == None:

            self.tabuleiro = getSudoku()
            print_board(self.tabuleiro)

        
    def preparar(self, tabuleiro):  #irá apagar os numeros de forma que seja possivel resolver o tabuleiro
        pass


t1 = Tabuleiro

#FAZER A GETMETODOS E A GETATRIBUTOS