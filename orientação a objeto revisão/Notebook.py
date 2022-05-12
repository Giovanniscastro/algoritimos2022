from Computador import Computador

class Notebook( Computador ):

    def __init__(self, modelo, cor, preco, tempoDeBateria):
        self._modelo = modelo
        self._cor = cor
        self.preco = preco
        self.__tempoDeBateria = tempoDeBateria


    @property 
    def modelo(self):
        pass

    @modelo.setter
    def modelo(self, valor):
       pass

    @property 
    def cor(self):
        pass

    @cor.setter
    def cor(self, valor):
        pass

    @property 
    def preco(self):
        pass

    @preco.setter
    def preco(self, valor):
        pass

    def getInformacoes(self): #reimplementa
        super().getInformacoes()
        print("Tempo de Bateria: " , self.__tempoDeBateria )


    def cadastrar(self):
        print("Cadastrado com sucesso!")
