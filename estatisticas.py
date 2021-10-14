from log import *
import numpy as np
import matplotlib.pyplot as plt

class Estatisticas():
    '''
    Essa classe tem como função produzir um conjunto de métodos para a manipulação de arrays
    utilizando-se de matplotlib e numpy.

    Usando das partidas do histórico do usuário, para criar gráficos com quantidade de partidas
    ganhas, erros, desistências e tempo médio.

            Estatísticas importantes:
                -Número de jogos
                -Quantidade de vitórias
                -Quantidade de desistências
                -Quantidade de erros
                -tempo médio


        -1 = o último elemento se ele resolveu, errou a resolução ou desistiu da partida. (ganhou = 1, desistiu = 0, perdeu = -1)
        -2 = o penúltimo o tempo que ele demorou para fechar ou desistir.
        -3 = o antipenultimo a quantidade de erros que ele teve quando fechou o tabuleiro
        -4 = a quantidade de dicas usadas
        [0:-3] = e entre todos esses o histórico de jogadas.

        A __init__ vai abrir o arquivo(normalmente vai ser o historico.txt), colocalo em listas criar outras
        listas para manipulação
        então ela endereça para lista removendo o primeiro elemento que será o nome do jogador.
        Para cada numero do final da lista ela separa e adiciona a uma lista correspondente.
        O final do algoritmo transforma as listas em array. Para serem usados na função.
    '''
    def __init__(self, arquivo):

        arq = open(arquivo, 'r')
        numero_de_partidas_lista = []
        leitura = arq.readlines()
        leia = []

        for i in range(0, len(leitura)):
            aux = leitura[i].split(' ')
            leia.append(aux[1:])

        tamanho = len(leia)
        resultado, tempo, qnt_erro, qnt_dicas = [],[],[],[]

        for i in range(-4, 0):
            for j in range(0, tamanho):

                elem = leia[j][i]

                if j+1 not in numero_de_partidas_lista:

                    numero_de_partidas_lista.append(j+1)

                if i == -1:

                    resultado.append(int(elem))
                
                if i == -2:
                    
                    tempo.append(int(elem)) 

                if i == -3:

                    qnt_erro.append(int(elem))
                
                if i == -4:

                    qnt_dicas.append(int(elem))

        self.resultado = np.array([resultado])
        self.tempo = np.array([tempo])
        self.qnt_erro = np.array([qnt_erro])
        self.numero_de_partidas = np.array([numero_de_partidas_lista])
        self.qnt_dicas = np.array([qnt_dicas])

    def grafico(self, eixo_x, eixo_y):
        '''
        Essa função tem como objetivo traçar o gráfico utilizando-se dos array do __init__
        ele tem os eixos aceito em dicionário, a partir disso ele verifica se os eixos são corretos.

        configura a parte do subplots, adiciona eixos.

        O resultado das partidas tem que ter legenda e cores diferentes, para isso foi criado dois if para
        que seja feito de um método diferente a plotagem. Ao final disso é retornado True e plotado o gráfico.
        '''

        eixos_aceitos = {
        'Quantidade de jogos': self.numero_de_partidas,
        'Resultados das partidas': self.resultado,
        'Quantidade de erros': self.qnt_erro,
        'Tempo': self.tempo,
        'Quantidade de dicas': self.qnt_dicas
        }

        if (eixo_x and eixo_y) in eixos_aceitos:

            fig, ax = plt.subplots()

            if eixo_x == 'Tempo':
                plt.xlabel(f'{str(eixo_x)}[s]')
                plt.ylabel(str(eixo_y))

            elif eixo_y == 'Tempo':
                plt.ylabel(f'{str(eixo_y)}[s]')
                plt.ylabel(str(eixo_y))

            else:
                plt.xlabel(str(eixo_x))
                plt.ylabel(str(eixo_y))

            if eixo_x == 'Resultados das partidas':
                
                lista1 = self.resultado[0]
                aux2 = eixos_aceitos[eixo_y]
                lista2 = aux2[0]

                vitorias, desistencias, derrotas, partidas1, partidas2, partidas3 = [],[],[],[],[],[]

                for i in range(np.size(self.resultado)):
                    
                    k = lista1[i]

                    if k == 1:

                        vitorias.append(lista1[i])
                        partidas1.append(lista2[i])
                       


                    if k == 0:

                        desistencias.append(lista1[i])
                        partidas2.append(lista2[i])
                        


                    if k == -1:

                        derrotas.append(lista1[i])
                        partidas3.append(lista2[i])

                print(partidas1)
                print(partidas2)
                print(partidas3)

                vitorias = np.array([vitorias])
                desistencias = np.array([desistencias])
                derrotas = np.array([derrotas])
                partidas1 = np.array([partidas1])
                partidas2 = np.array([partidas2])
                partidas3 = np.array([partidas3])

                ax.plot(vitorias, partidas1, 'go', label = 'Vitórias')
                ax.plot(desistencias, partidas2, 'yo', label = 'Desistências')
                ax.plot(derrotas, partidas3, 'ro', label = 'Derrotas')
                
                plt.legend(['Vitórias', 'Desistências', 'Derrotas'], loc=1)

            elif eixo_y == 'Resultados das partidas':

                lista1 = self.resultado[0]
                aux2 = eixos_aceitos[eixo_x]
                lista2 = aux2[0]
                vitorias, desistencias, derrotas, partidas1, partidas2, partidas3 = [],[],[],[],[],[]

                for i in range(np.size(self.resultado)):
                    
                    k = lista1[i]

                    if k == 1:

                        vitorias.append(lista1[i])
                        partidas1.append(lista2[i])
                       


                    if k == 0:

                        desistencias.append(lista1[i])
                        partidas2.append(lista2[i])
                        


                    if k == -1:

                        derrotas.append(lista1[i])
                        partidas3.append(lista2[i])

                print(partidas1)
                print(partidas2)
                print(partidas3)

                vitorias = np.array([vitorias])
                desistencias = np.array([desistencias])
                derrotas = np.array([derrotas])
                partidas1 = np.array([partidas1])
                partidas2 = np.array([partidas2])
                partidas3 = np.array([partidas3])

                ax.plot(partidas1, vitorias, 'go', label = 'Vitórias')
                ax.plot(partidas2, desistencias, 'yo', label = 'Desistências')  
                ax.plot(partidas3, derrotas, 'ro', label = 'Derrotas')
                
                plt.legend('Vitórias', 'Desistências', 'Derrotas', loc='best')

            else:

                aux = Estatisticas('historico.txt')
                media = aux.media(eixo_y)

                if media != False:

                    arrayx = np.linspace(0, np.max(eixos_aceitos[eixo_x]))
                    arrayy = np.linspace(media, media, np.size(arrayx))

                    ax.plot(eixos_aceitos[eixo_x], eixos_aceitos[eixo_y], 'bo')

                    if eixo_y == 'Quantidade de erros':

                        ax.plot(arrayx, arrayy, 'r-', label = 'Média de erros')
                        plt.legend(loc='best')

                    else:

                        ax.plot(arrayx, arrayy, 'r-', label = f'Média de {eixo_y}')
                        plt.legend(loc='best')

                else:

                    ax.plot(eixos_aceitos[eixo_x], eixos_aceitos[eixo_y], 'bo')

            plt.show()
        
        return True
    
    def media(self, opcao): #testar essa função 
        '''
            Esta função a partir de uma opção em str ele retorna a média de uma dada estatística do jogador.
            Checa os eixos de entrada para selecionar o array corretamente. Em seguida faz a soma interna do array
            e divide pelo tamanho do mesmo.
        '''

        eixos_aceitos = {
        'Quantidade de erros': self.qnt_erro,
        'Tempo': self.tempo,
        'Quantidade de dicas': self.qnt_dicas
        }

        if opcao in eixos_aceitos:

            soma = np.sum(eixos_aceitos[opcao])

            return soma/np.size(eixos_aceitos[opcao])

        else:
            return False

    def porcentagens(self): # A função apresenta um bug, tem que dar fix
        '''
        Entrega as estatisticas de porcentagens de vitórias, derrotas e desistencias. Coloca os três resultados
        1, 0, -1 em uma lista e roda um for para cada i ele conta a qunatidade de ocorrencia de um item i
        e faz os calculos de porcentagem.
        '''

        for i in range(-1, 2):

            if i == 1:
                qnt = np.count_nonzero(self.resultado == i)
                print(qnt)
                porcentagem_de_wins = (qnt/np.size(self.resultado))*100

            elif i == 0:
                qnt = np.count_nonzero(self.resultado == i)
                porcentagem_de_desistencias = (qnt/np.size(self.resultado))*100

            elif i == -1:
                qnt = np.count_nonzero(self.resultado == i)
                porcentagem_de_derrotas = (qnt/np.size(self.resultado))*100

        return porcentagem_de_wins, porcentagem_de_desistencias, porcentagem_de_derrotas



            

#e1 = Estatisticas()
#e1.grafico('Quantidade de jogos', 'Resultados das partidas')

#TUDO FUNCIONANDO, VER MAIS TARDE SE PODE ADICIONAR COISAS COMO SOMENTE VITÓRIAS, DERROTAS E DESISTENCIAS, ETC
#Ver se é possível adicionar uma linha de média sobre a estatística do eixo x
    