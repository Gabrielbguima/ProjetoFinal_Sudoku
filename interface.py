import os
from excecoes import *
from log import *
from msvcrt import getch
from tabuleiro import *
from estatisticas import *
from loadsave import *
from mecanicas import *
import time

class Interface():
    '''
    representa o que opera atrás da tela do usuario. Possui funções que auxiliam a construção da tela para o jogador,
    além de contruí-la.
    '''
    
    tabelaCaracteres = {chr(x) : x for x in range(256)}
    atributos = {'nome_do_jogo'}
    metodos = {'limpartela', 'telaInicial', 'opcaoEscolhida','jogando','getAtributos','getMetodos', 'getManual'}

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

        while True: #Loop deixa o menu rodando o tempo todo

            Interface.limparTela()

            print(f'{nome_do_jogo}: MENU PRINCIPAL')
            print('\t')

            if i == 0:
                print('>>>Novo jogo')
            else:
                print('Novo Jogo')

            if i == 1:
                print('>>>Continuar')
            else:
                print('Continuar')
            
            if i == 2:
                print('>>>Estatisticas')
            else:
                print('Estatisticas')

            if i == 3:
                print('>>>Manual')
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
        '''
        Executa as opções do menu principal, assim que o usuário pressiona a tecla Enter para confirmar.
        Recebe um parâmetro de entrada no caso foi feito para funcionar com o contador i da função telaInicial.
        Quando i igual a:
            0 = Inicia-se o jogo, printando o tabuleiro e preparando-o chamando a classe tabuleiro.
            1 = carrega o tabuleiro que estava antes do jogo fechar ou o jogador decidir sair da partida.
            2 = Carrega as estatísticas, mostra as opções de estatística que delas plotam gráficos correspondentes
            as opções.
            3 = Mostra na tela o manual do jogo.
        '''

        if input == 0:  #opção novo jogo
            
            Interface.limparTela()
            try:
                verificar = open('tabuleiroAtual.txt', 'r')
                aux = verificar.readlines()
                
                if aux[0] == '0':

                    board = Tabuleiro()
                    preparado = Tabuleiro.preparar(board)
                    tabuleiro = Tabuleiro.tabuleiroResolvido(board)
                    Interface.jogando(preparado, tabuleiro)

                else:

                    u = 0

                    while True:

                        Interface.limparTela()
                        print('Você já tem um jogo em andamento deseja encerrar?')

                        if u == 0:
                            print('>>>Não (inicie o jogo pelo carregar)')
                            print('Sim')
                        else:
                            print('Não')
                            print('>>>Sim (Seu jogo anterior não será salvo)')

                        c = getch()

                        if c == b'\xe0':
                            c += getch()

                        if c == b'\xe0H':   #tecla seta para baixo do teclado
                            u-=1
                            if u == -1:
                                u = 2

                        elif c == b'\xe0P': #tecla seta para cima do teclado
                            u+=1
                            u%=3
                        
                        if c == b'\r':  #Se c for a tecla enter
                            
                            if u == 0:
                                break

                            if u == 1:
                                reescrever = open('tabuleiroAtual.txt', 'w')
                                reescrever.write('0')
                                break

            except FileNotFoundError:

                log.addLog('FileNotFoundError')

                board = Tabuleiro()
                preparado = Tabuleiro.preparar(board)
                tabuleiro = Tabuleiro.tabuleiroResolvido(board)
                Interface.jogando(preparado, tabuleiro)


        elif input == 1: #opção continua, carrega um jogo parado

            try:

                #linhas que transforamam o texto do .txt em listas com inteiros novamente.

                numeros = {'0':0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}

                lista = [[],[],[],[],[],[],[],[],[]]
                lista2 = [[],[],[],[],[],[],[],[],[]]

                leia = open('tabuleiroAtual.txt','r')
                leia2 = open('tabuleiroResolvido.txt', 'r')

                leitura = leia.readlines()
                leitura2 = leia2.readlines()

                if leitura[0] == '0':   #caso o arquivo esteja vazio

                    ImpossivelCarregar()
                    log.addLog('ImpossivelCarregar')

                else:

                    for i in range(len(leitura)):
                        for j in range(len(leitura[i])):
        
                            if leitura[i][j] in numeros:
                                aux = numeros[leitura[i][j]]
                                lista[i].append(aux)
                    
                    for i in range(len(leitura2)):
                        for j in range(len(leitura2[i])):
        
                            if leitura2[i][j] in numeros:
                                aux2 = numeros[leitura2[i][j]]
                                lista2[i].append(aux2)
                    
                    preparado = lista
                    tabuleiro = lista2
                    Interface.jogando(preparado, tabuleiro)

            except FileNotFoundError:   #retorna erro caso o jogador tente acessar essa função antes de jogar

                log.addLog('ImpossivelCarregar')
                ImpossivelCarregar()
           

        elif input == 2:    #opção estatísticas

            try:

                loadSave('historico.txt')   #load no histórico

                j = 0
                k = 0

                a = Estatisticas('historico.txt')
                por = a.porcentagens()
                media_erros = a.media('Quantidade de erros')
                media_tempo = a.media('Tempo')
                media_dicas = a.media('Quantidade de dicas')

                while True:

                    Interface.limparTela()

                    print('==SUAS ESTATÍSTICAS==')
                    print('\t')
                    print('Estatísticas gerais:')
                    print('\t')
                    print(f'Vitórias---------{por[0]:0.2f}%\nDesistências-----{por[1]:0.2f}%\nDerrotas---------{por[2]:0.2f}%')
                    print('\t')
                    print(f'Média de Erros---{media_erros:0.2f}\nMédia de tempo---{media_tempo:0.2f} segundos\nMédia de dicas---{media_dicas:0.2f}')
                    print('\t')
                    
                    #cada número de k é uma opção de gráfico que pode ser plotado

                    if k == 1:  

                        print('Opções de gráficos:')
                        print('\t')
                        print('Escolha sua segunda opção:')
                        print('\t')

                    else:
            
                        print('Opções de gráficos:')
                        print('\t')
                        print('Qual gráfico você deseja? Selecione duas.')
                        print('\t')

                    if j == 0:
                        print('>>>Quantidade de jogos')
                    else:
                        print('Quantidade de jogos')
                    
                    if j == 1:
                        print('>>>Resultados das partidas')
                    else:
                        print('Resultados das partidas')
                    
                    if j == 2:
                        print('>>>Quantidade de erros')
                    else:
                        print('Quantidade de erros')

                    if j == 3:
                        print('>>>Tempo')
                    else:
                        print('Tempo')
                    
                    if j == 4:
                        print('>>>Quantidade de dicas')
                    else:
                        print('Quantidade de dicas')
                    
                    c = getch()

                    if c == b'\x1b': #se c for a tecla ESC será encerrado o loop
                        break

                    if c == b'\xe0':
                        c += getch()

                    if c == b'\xe0H':   #tecla seta para baixo do teclado
                        j-=1
                        if j == -1:
                            j = 4

                    elif c == b'\xe0P': #tecla seta para cima do teclado
                        j+=1
                        j%=5
                    
                    if c == b'\r':  #Se c for a tecla enter

                        opcoes = {
                            0 :'Quantidade de jogos',
                            1 :'Resultados das partidas',
                            2 :'Quantidade de erros',
                            3 :'Tempo',
                            4:'Quantidade de dicas'
                        }

                        if k == 0:

                            opcao1 = opcoes[j]

                        elif k > 0:

                            opcao2 = opcoes[j]

                            try:
                                a = Estatisticas('historico.txt')
                                a.grafico(opcao1, opcao2)
                                break

                            except FileNotFoundError:
                                loadSave()
                                log.addLog('FileNotFoundError')

                        k = 1 

            except ZeroDivisionError:

                log.addLog('ZeroDivisionError')
                log.addLog('ImpossivelCarregar')
                ImpossivelCarregar()          

            except FileNotFoundError:   #retorna erro caso o jogador tente acessar cedo demais

                print('Não há estatísticas, você ainda não jogou.')
                log.addLog('FileNotFoundError')

        elif input == 3:

            Interface.limparTela()
            p = 0
            print('PRESSIONE ENTER')

            while True:
                
                k = getch()

                if k == b'\x1b': #se c for a tecla ESC será encerrado o loop
                    break

                if k == b'\r':  #Se c for a tecla enter
                    p += 1
                    if p == 9:
                        break

                Interface.printmanual(p)

    def jogando(preparado, board):
        '''
        funcão que deixa o jogo funcionando em loop, reagindo a cada input do jogador seja de setas, numeros,
        backspace e etc.
        '''
        i = 0

        Mecanicas.tabuleiroOriginal(preparado)
        erros = 0
        dicas = 0
        tempo = 0
        desistiu = False
        concluiu = False
        perdeu = False
        comecou = time.time()

        while True: #deixa o tabuleiro sendo exibido na tela em loop


            if concluiu == True or desistiu == True or perdeu == True:
                
                if concluiu == True:

                    while True:
                        
                        terminou = time.time()
                        tempo = int(terminou) - int(comecou)

                        c = getch()
                        print(f'Você teve: {erros} erros')
                        print('\t')
                        print(f'Você usou: {dicas} dicas')
                        print('\t')
                        print(f'Com um tempo de:{tempo:0.2f} segundos')

                        if c == b'\x1b': #se c for a tecla ESC será encerrado o loop
                            #reinicia o tabuleiro e escreve as estatísticas quando se encerra
                            reiniciar = open('tabuleiroResolvido.txt', 'w')
                            reiniciar.write('')
                            reiniciar.close()

                            hist = open('historico.txt', 'a')
                            hist.write(str(dicas) + ' ')
                            hist.write(str(erros) + ' ')
                            hist.write(str(tempo) + ' ')
                            hist.write(str(1) + '\n')

                            reescrever = open('tabuleiroAtual.txt', 'w')
                            reescrever.write('0')
                            break

                        elif c == b'\r':  #Se c for a tecla enter

                            reiniciar = open('tabuleiroResolvido.txt', 'w')
                            reiniciar.write('')
                            reiniciar.close()

                            hist = open('historico.txt', 'a')
                            hist.write(str(dicas) + ' ')
                            hist.write(str(erros) + ' ')
                            hist.write(str(tempo) + ' ')
                            hist.write(str(1) + '\n')

                            
                            reescrever = open('tabuleiroAtual.txt', 'w')
                            reescrever.write('0')
                            break

                        else:
                            pass
                    break
                else:

                    Interface.limparTela()
            
                    reescrever = open('tabuleiroAtual.txt', 'w')
                    reescrever.write('0')

                    break

            else:
                
                Interface.limparTela()
                print_board(preparado)
                concluiu = Tabuleiro.terminou(preparado)    #marca se o tabuleiro já foi concluido

                print('\t')
                print(f'Erros:{erros}/10 Dicas:{dicas}/3 Tempo:{(time.time() - comecou):0.3f}')
                print('\t')
                print('---------------------------------------------------------------------')

                if i == 0:
                    print('>>>Nova jogada')
                else:
                    print('Nova jogada')
                
                if i == 1:
                    print('>>>Apagar jogada')
                else:
                    print('Apagar jogada')

                if i == 2:
                    print('>>>Dica')
                else:
                    print('Dica')
                
                if i == 3:
                    print('>>>Desistir')
                else:
                    print('Desistir')
                
                if i == 4:
                    print('>>>Voltar ao Menu Principal')
                else:
                    print('Voltar ao Menu Principal')

                c = getch()


                if c == b'\r':  #Se c for a tecla enter
                    if i == 0:  #opção de fazer uma jogada
                        while True:
                            #mantém em loop a função
                            Interface.limparTela()
                            print_board(preparado)
                            print('\t')
                            c = getch()

                            if c == b'\x1b': #se c for a tecla ESC será encerrado o loop
                                break

                            else:

                                try:
        
                                    print('Digite um número representando a jogada')
                                    x = int(input())
                                    print('Número da linha:')
                                    y = int(input())
                                    print('Número da coluna:')
                                    z = int(input())
                                    m = Mecanicas
                                    y = int(y)
                                    z = int(z)

                                    preparado = m.jogada(x,(y,z), preparado)
                                    m  = loadSave('historico.txt')
                                    m.salvarJogada(str((x,y,z)))
                                    m.salvarTabuleiro(preparado)
                                    erros = Mecanicas.errou(preparado, board, erros)#verifica se está errada

                                    if erros == 10:  #caso seja igual a 10 o jogo é encerrado
                                        
                                        Interface.limparTela()

                                        terminou = time.time()
                                        tempo = int(terminou) - int(comecou)

                                        print('Você perdeu :(')

                                        reiniciar = open('tabuleiroResolvido.txt', 'w')
                                        reiniciar.write('')
                                        reiniciar.close()

                                        hist = open('historico.txt', 'a')
                                        hist.write(str(dicas) + ' ')
                                        hist.write(str(erros) + ' ')
                                        hist.write(str(tempo) + ' ')
                                        hist.write(str(-1) + '\n')
                                        perdeu = True

                                        break

                                    else:

                                        break

                                except ValueError:

                                    print('Deve ser obrigatóriamente um número.')
                                    break

                    elif i == 1:    #opção apagar jogada
                        
                        while True:

                            Interface.limparTela()
                            print_board(preparado)
                            print('\t')

                            c = getch()

                            if c == b'\x1b': #se c for a tecla ESC será encerrado o loop
                                break

                            else:

                                try:

                                    print('Qual casa deve ser apagada?')
                                    print('\t')
                                    print('Número da linha:')
                                    y = int(input())
                                    print('Número da coluna:')
                                    z = int(input())
                                    m = Mecanicas
                                    y = int(y)
                                    z = int(z)

                                    preparado = m.apagarjogada((y,z), preparado)

                                    m  = loadSave('historico.txt')
                                    m.salvarJogada(str(('apagado',y,z)))
                                    m.salvarTabuleiro(preparado)

                                    break
                                
                                except ValueError:

                                    print('Deve ser obrigatóriamente um número.')
                                    break  

                    elif i == 2:    #opção dica, se for clicada será dada uma dica aleatoriamente no tabuleiro

                        num, linha, coluna, qnt_dica = Mecanicas.dicas(preparado, board, dicas)
                        print(num, linha, coluna, qnt_dica)
                        dicas = qnt_dica

                        preparado = Mecanicas.jogada(num, (linha, coluna), preparado)

                        m  = loadSave('historico.txt')
                        m.salvarJogada(str((num,linha,coluna)))
                        m.salvarTabuleiro(preparado)

                        final = find_empty(preparado)

                        if final == None:
                            print('Você ganhou!!')
                            concluiu = True
                            break
                        
                    elif i == 3:    #opção desistir, vai perguntar se quer desistir e encerrar o jogo

                        j = 0

                        while True:
                            
                            Interface.limparTela()

                            print('Você deseja mesmo desistir?')
                            if j == 0:
                                print('>>>não \t sim')
                            elif j == 1:
                                print('não \t >>>sim')
                            
                            c = getch()

                            if c == b'\xe0':
                                c += getch()

                            if c == b'\xe0H':   #tecla seta para baixo do teclado
                                j-=1
                                if j == -1:
                                    j = 2

                            elif c == b'\xe0P': #tecla seta para cima do teclado
                                j+=1
                                j%=3
                        
                            if c == b'\r':

                                if j == 0:
                                    break

                                elif j == 1: #processo de finalizar o salvando no histórico e limpando o tabuleiroAtual
                                    terminou = time.time()
                                    tempo = int(terminou) - int(comecou)

                                    reiniciar = open('tabuleiroResolvido.txt', 'w')
                                    reiniciar.write('')
                                    reiniciar.close()
                                    
                                    hist = open('historico.txt', 'a')
                                    hist.write(str(dicas) + ' ')
                                    hist.write(str(erros) + ' ')
                                    hist.write(str(tempo) + ' ')
                                    hist.write(str(0) + '\n')
                                    desistiu = True
                                    break

                    elif i == 4:    #opção voltar ao menu principal

                        try:
                            m = loadSave('historico.txt')
                            m.salvarTabuleiro(preparado)
                            break

                        except FileNotFoundError:

                            log.addLog('FileNotFoundError')
                            m = loadSave()
                            m = loadSave('historico.txt')
                            m.salvarTabuleiro(preparado)

                if c == b'\xe0':
                    c += getch()

                if c == b'\xe0H':   #tecla seta para baixo do teclado
                    i-=1
                    if i == -1:
                        i = 4

                elif c == b'\xe0P': #tecla seta para cima do teclado
                    i+=1
                    i%=5
                

    def printmanual(input):
        '''
        Função criada para printar o manual 'interativo'
        '''

        if input == 0:
            print('MANUAL DO SUDOKU:')
            print('\t')
            print('Bem-Vindo!! :D')
            print('\t')

            return True

        if input == 1:
            print('\t')
            print('O Sudoku é um jogo que requer algum tempo e raciocínio')
            return True

        if input == 2:
            print('\t')
            print('Ele geralmente é composto de uma tabela de 9x9')
            return True

        if input == 3:
            print('\t')
            print('A qual é composta por 9 grades')
            print('\t')
            print('\t\t9 8 1  | 5 7 2  | 4 6 3')
            print('\t\t4 0 2  | 9 8 0  | 7 1 5')
            print('\t\t5 7 6  | 3 0 0  | 8 0 0')
            print('\t\t- - - - - - - - - - - - -')
            print('\t\t3 0 5  | 0 0 9  | 6 7 0')
            print('\t\t2 9 8  | 0 0 7  | 1 0 0')
            print('\t\t1 0 0  | 0 0 8  | 5 0 0')
            print('\t\t- - - - - - - - - - - - -')
            print('\t\t6 0 4  | 0 0 5  | 0 8 7')
            print('\t\t8 1 3  | 7 0 4  | 0 5 6')
            print('\t\t7 5 0  | 8 0 3  | 0 4 0')
            return True

        if input == 4:
            print('\t')
            print('Que respetivamente têm 9 células.')
            print('\t')
            print('\t\t9 8 1  |')
            print('\t\t4 0 2  |')
            print('\t\t5 7 6  |')
            print('\t\t- - - - ')
            return True

        if input == 5:
            print('\t')
            print('A ideia principal do jogo é que o jogador preencha a tabela com números de 1 a 9')

        if input == 6:
            print('\t')
            print('Os espações vazios são os zeros:')
            print('\t')
            print('\t\t0 0 0  |')
            print('\t\t0 0 0  |')
            print('\t\t0 0 0  |')
            print('\t\t- - - - ')
            print('\t')
            print('sem que haja quaisquer repetições de números na mesma linha ou grade')
            return True

        if input == 7:
            print('\t')
            print('Nesse Sudoku para preencher é necessário usar coordenadas')
            print('\t')
            print('De 1 a 9, ESQUERDA para a DIREITA')
            print('\t')
            print('De 1 a 9,  CIMA para BAIXO')
            print('\t')
            print('Essas coordenadas não aparecerão no jogo rodando')

        if input == 8:
            print('\t')
            print('Se cumprir todas estas regras e conseguir preencher a tabela, então o jogo está ganho!')
            print('\t')
            print('\t\t1 2 3    4 5 6    7 8 9 Coordenadas')
            print('\t')
            print('\t\t7 5 3  | 6 8 9  | 1 2 4\t 1')
            print('\t\t6 9 2  | 7 4 1  | 5 8 3\t 2')
            print('\t\t4 8 1  | 5 2 3  | 7 9 6\t 3')
            print('\t\t- - - - - - - - - - - - -')
            print('\t\t8 3 7  | 4 1 2  | 9 6 5\t 4')
            print('\t\t5 2 6  | 3 9 7  | 8 4 1\t 5')
            print('\t\t9 1 4  | 8 5 6  | 3 7 2\t 6')
            print('\t\t- - - - - - - - - - - - - ')
            print('\t\t2 4 9  | 1 3 8  | 6 5 7\t 7')
            print('\t\t3 7 5  | 9 6 4  | 2 1 8\t 8')
            print('\t\t1 6 8  | 2 7 5  | 4 3 9\t 9')
            print('\t')
            print('EXEMPLO DE TABULEIRO RESOLVIDO ^^ :D')
            return True

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
        manual['telaInicial']           = Interface.telaInicial.__doc__
        manual['jogando']               = Interface.jogando.__doc__
        manual['limparTela']            = Interface.limparTela.__doc__
        manual['getAtributos']          = Interface.getAtributos.__doc__
        manual['getMetodos']            = Interface.getMetodos.__doc__
        manual['getManual']             = Interface.getManual.__doc_
                
        return manual

#TERMINAR A QUARTA OPÇÃO DE MANUAL
# menuprincipal, telapause, telacarregar, telasalvar, opções
#FAZER A GETMETODOS E A GETATRIBUTOS

