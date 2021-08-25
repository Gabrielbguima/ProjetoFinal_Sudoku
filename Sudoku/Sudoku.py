# Document properties
'''
Este pograma contém um sudoku:

Sudoku, por vezes escrito Su Doku é um jogo baseado na colocação lógica de números. 
O objetivo do jogo é a colocação de números de 1 a 9 em cada uma das células vazias numa grade de 9x9,
constituída por 3x3 subgrades chamadas regiões. O quebra-cabeça contém algumas pistas iniciais, 
que são números inseridos em algumas células, de maneira a permitir uma indução ou dedução dos números em células que estejam vazias.
Cada coluna, linha e região só pode ter um número de cada um dos 1 a 9. Resolver o problema requer apenas raciocínio lógico e algum tempo.
'''

__author__ = 'Gabriel Batista Guimarães'
__copyright__ = 'Copyright_2021'
__credits__ = __author__
__license__ = 'Gabrielbguima'
__version__ = '1.0.0'
__maintainer__ = 'Gabriel_Guimarães' # Responsável por manter o programa funcionando
__email__ = 'gabrielbguima@poli.ufrj.br'
__status__ = 'Production'

from validSudoku import *
from tela import *
from tabuleiro import *
from jogador import *
from mecanicas import *

class Sudoku(Mecanicas):    #recebe as mecanicas do jogo

    def __init__(self, jogador = 1):    #recebe o parametro de jogadores, sempre 1.
        pass
    def solucao(self, solve):  #mostra a solução caso necessário
        pass
    def ganhou(self, find_empty):   #verifica e apresenta a mensagem que ganhou quando o jogador completa
        pass
        
    def __str__(self, funcao):  #representação em string
        manual = manual.Tela
        return (print(f'{funcao} : {manual[funcao]}'))
        
#tabuleiro virá do validSudoku