import os
from excecoes import ImpossivelCarregar
from log import *
from msvcrt import getch
from tabuleiro import *
from estatisticas import *
from loadsave import *

class Interface():
    '''
    representa o que opera atrás da tela do usuario
    '''
    
    tabelaCaracteres = {chr(x) : x for x in range(256)}
    atributos = {'nome_do_jogo'}
    metodos = {'limpartela', 'telaInicial', 'opcaoEscolhida'}

    def limparTela():

        """
        Esta função limpa toda a tela do console do Windows. 
        Com isso, é possível dar 'refresh' na tela a ser desenhada.
        """
        os.system('cls')
    
        return True

    
    def telaInicial(nome_do_jogo = 'Sudoku'):

        '''
            Essa classe deve printar a tela principal do jogo, ou seja o menu principal.
            Esse menu contém o nome do jogo e as opções disponíveis. Por exemplo:
            - Novo jogo
            - Continuar
            - Estatistica
            - Manual
            Utilizando-se o método getch() é feita a navegação dentro do menu, possibilitando escolher
            as opções disponíveis.
            Criou-se um contador i e para cada valor de i printaría-se uma tela diferente
            com o comando os.system chamamos o cls para limpar a tela. Então nós usamos o getch()
            para identificar a tecla pressionada pelo usuário, se forem as setas cima e baixo
            ela modifica o valor de i de acordo.
        '''

        i = 0

        while True:

            Interface.limparTela()

            print(f'{nome_do_jogo}: MENU PRINCIPAL')

            if i == 0:
                print('-->Novo jogo')
            else:
                print('Novo Jogo')

            if i == 1:
                print('-->Continuar')
            else:
                print('Continuar')
            
            if i == 2:
                print('-->Estatisticas')
            else:
                print('Estatisticas')
            
            if i == 3:
                print('-->Manual')
            else:
                print('Manual')

            c = getch()

            if c == b'\x1b': #se c for a tecla ESC será encerrado o loop
                break

            if c == b'\r':  #Se c for a tecla enter
                Interface.opcaoEscolhida(i)

            if c == b'\xe0':
                c += getch()

            if c == b'\xe0H':   #tecla seta para baixo do teclado
                i-=1
                if i == -1:
                    i = 3

            elif c == b'\xe0P': #tecla seta para cima do teclado
                i+=1
                i%=4

    def opcaoEscolhida(input):

        if input == 0:
            
            Interface.limparTela()

            board = Tabuleiro()
            Tabuleiro.preparar(board)

        elif input == 1:
            #Vai abrir o arquivo de carregar, preciso fazer as exceções para o caso de abrir errado e etc.
            try:
                tabuleiro = open('tabuleiroAtual.txt', 'r')
                continuar = tabuleiro
                tabuleiro.close()

                return continuar

            except FileNotFoundError:
                
                raise ImpossivelCarregar
           

        elif input == 2:

            loadSave('historico.txt')
            j = 0
            k = 0

            while True:

                Interface.limparTela()

                if k == 1:
                    print('Escolha sua segunda opção:')

                else:
                    print('Quais opções você deseja? Selecione duas')
                

                if j == 0:
                    print('-->Quantidade de jogos')
                else:
                    print('Quantidade de jogos')
                
                if j == 1:
                    print('-->Resultados das partidas')
                else:
                    print('Resultados das partidas')
                
                if j == 2:
                    print('-->Quantidade de erros')
                else:
                    print('Quantidade de erros')

                if j == 3:
                    print('-->tempo médio')
                else:
                    print('tempo médio')
                
                c = getch()

                if c == b'\x1b': #se c for a tecla ESC será encerrado o loop
                    break

                if c == b'\xe0':
                    c += getch()

                if c == b'\xe0H':   #tecla seta para baixo do teclado
                    j-=1
                    if j == -1:
                        j = 3

                elif c == b'\xe0P': #tecla seta para cima do teclado
                    j+=1
                    j%=4
                
                if c == b'\r':  #Se c for a tecla enter
                    opcoes = {
                        0 :'Quantidade de jogos',
                        1 :'Resultados das partidas',
                        2 :'Quantidade de erros',
                        3 :'tempo médio',
                    }

                    if k == 0:

                        opcao1 = opcoes[j]

                    elif k > 0:

                        opcao2 = opcoes[j]
                    
                        a = Estatisticas('historico.txt')
                        a.grafico(opcao1, opcao2)
                        break

                    k = 1
        '''elif input == 3:
            k = Sudoku
            k.__str__()

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
        manual['telaInicial']           = Interface.telaInicial.__doc__
        manual['opcaoEscolhida']        = Interface.opcaoEscolhida.__doc__
        manual['limparTela']            = Interface.limparTela.__doc__
        manual['getAtributos']          = Interface.getAtributos.__doc__
        manual['getMetodos']            = Interface.getMetodos.__doc__
        manual['getManual']             = Interface.getManual.__doc_
                
        return manual
#TERMINAR A QUARTA OPÇÃO DE MANUAL
# menuprincipal, telapause, telacarregar, telasalvar, opções
#FAZER A GETMETODOS E A GETATRIBUTOS

