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
        [0:-3] = e entre todos esses o histórico de jogadas.
    '''
    def __init__(self, arquivo = 'testeest.txt'):
        '''
            init para tratar a leitura de arquivos e a criação de arrays ou 1 array multidimensional com
            as informações das estatísticas
        '''
        arq = open(arquivo, 'r')
        numero_de_partidas_lista = []
        leitura = arq.readlines()
        leia = []

        for i in range(0, len(leitura)):
            aux = leitura[i].split(' ')
            leia.append(aux[1:])

        tamanho = len(leia)
        resultado, tempo, qnt_erro = [],[],[]

        for i in range(-3, 0):
            for j in range(0, tamanho):

                elem = leia[j][i]

                if j+1 not in numero_de_partidas_lista:

                    numero_de_partidas_lista.append(j+1)

                if i == -1:

                    resultado.append(int(elem))
                
                if i == -2:
                    
                    tempo.append(int(elem))  # VER A POSSIBILIDADE DE FAZER EM UM ARRAY SÓ, TAMBÉM COMO ADICIONARIA SEM CRIAR MULITPLOS ARRAYS

                if i == -3:

                    qnt_erro.append(int(elem))

        self.resultado = np.array([resultado])
        self.tempo = np.array([tempo])
        self.qnt_erro = np.array([qnt_erro])
        self.numero_de_partidas = np.array([numero_de_partidas_lista])

    def grafico(self, eixo_x, eixo_y):

        eixos_aceitos = {
        'Número de jogos': self.numero_de_partidas,
        'Resultados das partidas': self.resultado,
        'Quantidade de erros': self.qnt_erro,
        'tempo médio': self.tempo
        }

        if (eixo_x and eixo_y) in eixos_aceitos:

            fig, ax = plt.subplots()
            plt.xlabel(str(eixo_x))
            plt.ylabel(str(eixo_y))

            ax.plot(eixos_aceitos[eixo_x], eixos_aceitos[eixo_y], 'bo', linewidth = 1)

            plt.show()
        
        return True

e1 = Estatisticas()
e1.grafico('Número de jogos', 'Resultados das partidas')

#TUDO FUNCIONANDO, VER MAIS TARDE SE PODE ADICIONAR COISAS COMO SOMENTE VITÓRIAS, DERROTAS E DESISTENCIAS, ETC
    