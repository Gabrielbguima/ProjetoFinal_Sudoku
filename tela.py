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

        Interface.telaInicial()
            
        '''
            Quando for pressionado enter deve-se checar a numeração de i
            colocar os valores em array talvez? dar uma olhada mais tarde
            Ver a posição do gatilho no código por exemplo i == 0
            deve iniciar um novo jogo ou seja criar um sudoku dando gatilho em
            toda a cadeia que desenha o puzzle. Onde a parte de ativação deve ficar?
            Na classe sudoku e eu chamo a função tela para desenhar o menu de lá?
        '''

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
        
c = Tela()
c.visual()

'''
2. Crie dois atributos privados do tipo conjunto (set), que conterão os nomes dos atributos e dos métodos na classe de cada seção.

	3. Defina os métodos getAtributos() e getMetodos() que retornarão os respectivos conjuntos de nomes.

	4. Preencha o método mágico __str__, a ser acessado quando for dado um "print" de uma instância do seu jogo, que retornará uma string, convenientemente formatada, exibindo os atributos e os métodos com suas respectivas descrições.
'''
#Estatisticas caso acessado sem partidas anteriores deve devolver uma mensagem dizendo que não há partidas anteriores

#getch() para ENTER b'\r'