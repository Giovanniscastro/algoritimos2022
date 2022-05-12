from abc import ABCMeta, abstractmethod, abstractproperty


class ContaBancaria(metaclass=ABCMeta):

    @property
    def numero(self):
        pass

    @numero.setter
    @abstractmethod
    def numero(self, valor):
        pass

    @property
    def agencia(self):
        pass

    @agencia.setter
    @abstractmethod
    def agencia(self, valor):
        pass

    def imprimir(self):
        print("Numero: ", self.numero)
        print("Agencia: ", self.numero)

    @abstractmethod
    def Cadastrar(self):
        pass

    @abstractmethod
    def Depositar(self):
        pass
