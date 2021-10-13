from excecoes import CommandError
from validSudoku import *
from excecoes import *
from msvcrt import getch
from loadsave import *
from log import *

class Mecanicas:

    comandos_permitidos = {'1','2','3','4','5','6','7','8','9'}
    atributos = {'comando', 'comandos'}
    metodos = {'tempo', 'qntErros', 'teclas','getAtributos', 'getMetodos', 'getManual'}

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
        manual['telaInicial']           = Interface.telaInicial.__doc__
        manual['opcaoEscolhida']        = Interface.opcaoEscolhida.__doc__
        manual['limparTela']            = Interface.limparTela.__doc__
        manual['getAtributos']          = Interface.getAtributos.__doc__
        manual['getMetodos']            = Interface.getMetodos.__doc__
        manual['getManual']             = Interface.getManual.__doc_
                
        return manual
    
#movimento do jogador no tabuleiro
#números permitidos
#mensagem de erro
#casas erradas
#apagar (posso colocar voltar, usando o arquivo que armazena todas as jogadas)
#dicas
#sair
#desistir

#FAZER A GETMETODOS E GETATRIBUTOS