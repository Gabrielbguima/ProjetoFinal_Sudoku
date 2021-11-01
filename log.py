class log():
    '''
        Classe tem como objetivo armazenar exceções no código do Sudoku mesmo que estejam sendo corrigidas.
    '''
    metodos = {'__init__','addLog'}
    atributos = {'arqlog'}
    def __init__(self, arqlog = None):

        if arqlog == None:

            self.arqlog = open('log.txt', 'w')
            self.arqlog.close()

        else:

            self.arqlog = open(arqlog, 'r')
            self.arqlog.close()

    def addLog(erro):
        '''
        Essa função adiciona ao log.txt o erro que ocorreu executando o código.
        '''
        log = open('log.txt', 'a')
        log.write(f'{str(erro)}\n')
        log.close

    def getAtributos(self, atributos = atributos):
        return atributos
    
    def getMetodos(self, metodos = metodos):
        return metodos
    
    def getManual(self):
        """
            Esta função estática (chamada sempre através de Tela.getManual()) retorna um 
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        metodos = {'__init__','salvarJogada','salvarTabuleiro','salvarResolucao', 'getAtributos', 'getMetodos', 'getManual'}
        atributos = {'arquivo'}
        """
        manual = {}
        manual['__init__']              = log.__init__.__doc__
        manual['addLog']          = log.addLog.__doc__
        manual['getAtributos']          = log.getAtributos.__doc__
        manual['getMetodos']            = log.getMetodos.__doc__
        manual['getManual']             = log.getManual.__doc_
                
        return manual