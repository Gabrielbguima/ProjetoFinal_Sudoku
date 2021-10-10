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
from loadsave import *
from log import *

class Sudoku(Mecanicas, Jogador, Tabuleiro, Tela, loadSave, log):    #recebe as mecanicas do jogo

    def __init__(self, jogador = 1):    #recebe o parametro de jogadores, sempre 1.

        self.jogador = jogador.nome

    def solucao(self, tabuleiro):  #mostra a solução caso necessário
        '''
            Se a opção for desistir será exibido a solução do problema,
            talvez seja necessário mover essa opção posteriormente
        '''
        solucao = solve(tabuleiro)
        print_board(solucao)

        return True

    def ganhou(self):   #verifica e apresenta a mensagem que ganhou quando o jogador completa
        '''
        Compara o tabuleiro do jogador com a solução, se for igual retorna True, caso não retorna falso com
        uma mensagem dizendo que está incorreta a solução. Usando os métodos da validSudoku.
        '''
        pass

    def jogar(self, num, pos): 
        '''
        recebe um numero do 1 a 9, a função verificará se trata de um numero dentro dos paramentros do jogo
        e realizará a efetivação da jogada na posição selecionada
        '''        
        pass
    
    def apagarjogada(self, pos): 
        '''
        Pega uma posição do tabuleiro e o remove o seu numero
        tomar cuidado para não apagar uma posição que já é nativa do tabuleiro. Ou seja, pré configurada
        Qunado isso acontecer retornar uma mensagem de erro
        '''
        pass   

    def __str__(self):  #representação em string

        saida = ''
        manual = Tela.getManual

        saida += 'Manual da classe Tela\n'

        for chave in manual:
                f'{chave} : {manual[chave]}\n'

        saida +='\n'

        return saida

if __name__ == main:
    pass

#tenho que fazer a getMetodos e getAtributos