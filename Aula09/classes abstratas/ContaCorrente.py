from ContaBancaria import ContaBancaria


class ContaCorrente(ContaBancaria):

    def __init__(self, numero, agencia, codigo_corrente):
        self._numero = numero
        self._agencia = agencia
        self._codigo_corrente = codigo_corrente
       
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
    def codigo_corrente(self):
        return self._codigo_corrente

    @codigo_corrente.setter
    def codigo_corrente(self, valor):
        self._codigo_corrente = valor

    def Cadastrar(self):
        print("Conta Poupanca: ")
        super().Cadastrar()

    def CadastrarEspecifico(self):
        self.Cadastrar()
        print("Codigo Poupanca: ", self.codigo_corrente)

    def Depositar(self):
        print("Conta Poupanca: ")
        super().Depositar()

    def DepositarEspecifico(self):
        self.Depositar()
        print("Codigo Poupanca: ", self.codigo_corrente)