from excecoes import CommandError
from validSudoku import *
from excecoes import *
from msvcrt import getch
from loadsave import *
from log import *

class Mecanicas:

    comandos_permitidos = {'1','2','3','4','5','6','7','8','9'}

    def teclas(self, comando, comandos = comandos_permitidos):   #usando o getch será definida as funções das teclas nessa função
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
    
    
#movimento do jogador no tabuleiro
#números permitidos
#mensagem de erro
#casas erradas
#apagar (posso colocar voltar, usando o arquivo que armazena todas as jogadas)
#dicas
#sair
#desistir

#FAZER A GETMETODOS E GETATRIBUTOS