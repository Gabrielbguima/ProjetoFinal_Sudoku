from interface import *

class Tela(Interface):
    '''
    A tela recebe a interface que contém
    '''
    atributos = {'opcoes', 'nome_do_jogo', 'salvar', 'carregar'}
    metodos = {'__init__','__str__','opcao_escolhida','visual','getManual','getAtributos','getMetodos'}
    def __init__(self, opcoes = None, nome_do_jogo = 'Sudoku', salvar = None, carregar = None): #recebe o titulo, o tabuleiro salvo, e carrega ele
    
        self.nome_do_jogo = nome_do_jogo
        self.opcoes = opcoes
        self.salvar = salvar    #o tabuleiro onde o jogador parou
        
    def __str__(self): #método de representação em string
        pass
        
    def opcao_escolhida(self, opcoes):  #executa a opção que o usuario selecionou
        pass
    
    def visual(self, nome_do_jogo, opcoes):   #print a tela principal
        pass
    
    def getAtributos():
        return atributos
    
    def getMetodos():
        return metodos
    
    def getManual():
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
        manual['nome_do_jogo']          = '# Representa o título da tela'
        manual['opcoes']                = '# Representa a lista de opções do usuário'
        manual['getAtributos']          = Tela.getAtributos.__doc__
        manual['getMetodos']            = Tela.getMetodos.__doc__
        manual['getManual']             = Tela.getManual.__doc_
                
        return manual
        
        
'''
2. Crie dois atributos privados do tipo conjunto (set), que conterão os nomes dos atributos e dos métodos na classe de cada seção.

	3. Defina os métodos getAtributos() e getMetodos() que retornarão os respectivos conjuntos de nomes.

	4. Preencha o método mágico __str__, a ser acessado quando for dado um "print" de uma instância do seu jogo, que retornará uma string, convenientemente formatada, exibindo os atributos e os métodos com suas respectivas descrições.
'''
#menuprincipal, telasalvar, opções