from loadsave import *
import time
import numpy as np
import matplotlib as plt
from log import *

class Jogador():

    atributos = {'nome', 'erros', 'tempo'}
    metodos = {'historico', 'estatisticas','getMetodos', 'getAtributos'}

    def __init__(self, nome = '', erros = 0, tempo = 0):   #receberá dados do jogador, como quantidade de erros cometidos e o tempo dele de resolução    
        '''
        todo jogo feito por esse jogador estará em um txt, que é feito no loadsave
        esse txt em cada linha terá 1 partida, sendo;
        -1 = o último elemento se ele resolveu, errou a resolução ou desistiu da partida.
        -2 = o penúltimo o tempo que ele demorou para fechar ou desistir.
        -3 = o antipenultimo a quantidade de erros que ele teve quando fechou o tabuleiro
        [0:-3] = e entre todos esses o histórico de jogadas.
        '''
        if nome == '':

            self.nome = str(input('Qual é o seu nome?'))

        else:

            self.nome = nome

        self.arquivo = open('save.txt', 'r') 

    #Talvez esses métodos possam ser passados para uma classe estatisticas
    #dessa classe seria importada dentro do método construtor da classe jogador
    #que por sua vez passaria para a interface, como um perfil de um jogador.

    def getMetodos(self, metodos = metodos):
        return metodos
    
    def getAtributos(self, atributos = atributos):
        return atributos