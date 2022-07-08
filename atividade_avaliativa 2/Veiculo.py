from abc import ABCMeta, abstractmethod, abstractproperty


class Veiculo(metaclass=ABCMeta):

    def __init__(self, marca, modelo):
        print("debug1", marca, modelo)
        self._marca = marca
        self._modelo = modelo

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    def getInformacoes(self): #return
        print("Marca:", self.marca, " - ", "Modelo:", self.modelo, " - ", end=" ")



