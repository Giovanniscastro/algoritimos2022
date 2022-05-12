from abc import abstractmethod
from Computador import Computador

class Desktop( Computador ):

    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        self._modelo = modelo
        self._cor = cor
        self.preco = preco
        self._potenciaDaFonte = potenciaDaFonte

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

    @property 
    def potenciaDaFonte(self):
        pass

    @potenciaDaFonte.setter
    def potenciaDaFonte(self, valor):
        pass


    def getInformacoes(self): 
        super().getInformacoes()
        print("Potencia da Fonte:" , self._potenciaDaFonte )


    def cadastrar(self):
        print("informações casdastradas!")