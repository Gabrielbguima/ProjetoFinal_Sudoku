import os
from log import *

class Interface():
    '''
    representa o que opera atrás da tela do usuario
    '''
    
    tabelaCaracteres = {chr(x) : x for x in range(256)} 
    
    def opcoes(): #contém as opções do jogo
        pass
        
    def limpaTela():
        """
        Esta função limpa toda a tela do console do Windows. 
        Com isso, é possível dar 'refresh' na tela a ser desenhada.
        """
        os.system('cls')
        
        return True
        
        
#criar classe tela, essa interface vai levar as letras funções de mover e etc
# menuprincipal, telapause, telacarregar, telasalvar, opções
#FAZER A GETMETODOS E A GETATRIBUTOS

