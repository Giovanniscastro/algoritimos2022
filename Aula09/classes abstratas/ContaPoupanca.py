#from abc import abstractmethod
from ContaBancaria import ContaBancaria


class ContaPoupanca(ContaBancaria):

    def __init__(self, numero, agencia, codigo_poupanca):
        self._numero = numero
        self._agencia = agencia
        self._codigo_poupanca = codigo_poupanca

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        self._numero = valor

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, valor):
        self._agencia = valor

    @property
    def codigo_poupanca(self):
        return self._codigo_poupanca

    @codigo_poupanca.setter
    def codigo_poupanca(self, valor):
        self._codigo_poupanca = valor

    def Cadastrar(self):
        print("Conta Poupanca: ")
        super().Cadastrar()

    def CadastrarEspecifico(self):
        self.Cadastrar()
        print("Codigo Poupanca: ", self.codigo_poupanca)

    def Depositar(self):
        print("Conta Poupanca: ")
        super().Depositar()

    def DepositarEspecifico(self):
        self.Depositar()
        print("Codigo Poupanca: ", self.codigo_poupanca)