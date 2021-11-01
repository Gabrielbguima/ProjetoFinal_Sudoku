from interface import *
from msvcrt import getch
import os
from log import *

class Tela(Interface):
    '''
    A tela recebe a interface que contém
    '''

    atributos = {'opcoes', 'nome_do_jogo'}
    metodos = {'__init__','__str__','opcao_escolhida','visual','getManual','getAtributos','getMetodos'}
    
    def __init__(self, opcoes = None, nome_do_jogo = 'Sudoku'):
    
        self.nome_do_jogo = nome_do_jogo
        self.opcoes = ['Novo jogo', 'Continuar', 'Estatísticas', 'Manual']
        
    def __str__(self): #método de representação em string
        pass
    
    def visual(self, nome_do_jogo = 'Sudoku'):   #print a tela principal
        '''
            Essa função tem como objetivo excutar a parte visual para o jogador, usando métodos da classe interface
            para gerar todos menus, opções inicializações e etc para o usuário.
        '''

        Tela.telaInicial()
        

    def getAtributos(self, atributos = atributos):
        return atributos
    
    def getMetodos(self, metodos = metodos):
        return metodos
    
    def getManual(self):
        """
            Esta função estática (chamada sempre através de Tela.getManual()) retorna um 
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        """
        manual = {}
        manual['__init__']              = Tela.__init__.__doc__
        manual['__str__']               = Tela.__str__.__doc__
        manual['visual']                = Tela.visual.__doc__
        manual['opcao_escolhida']       = Tela.opcao_escolhida.__doc__
        manual['getManual']             = Tela.getManual.__doc__
        manual['nome_do_jogo']          = Tela.nome_do_jogo
        manual['opcoes']                = Tela.opcoes
        manual['getAtributos']          = Tela.getAtributos.__doc__
        manual['getMetodos']            = Tela.getMetodos.__doc__
        manual['getManual']             = Tela.getManual.__doc_
                
        return manual