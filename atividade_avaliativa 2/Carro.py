from Veiculo import Veiculo


class Carro( Veiculo ):

    def __init__(self, marca, modelo, qtd_portas):
        super().__init__(marca, modelo)	
        self._qtd_portas = qtd_portas

    @property
    def qtd_portas(self):
        return self._qtd_portas

    def getInformacoes(self): #reimplementa
        super().getInformacoes()
        print("Quantidade de portas: ", self.qtd_portas)



