from Veiculo import Veiculo


class Drone(Veiculo):

    def __init__(self, marca, modelo, qtd_helices):
        print("debug2", marca, modelo)
        super().__init__(marca, modelo)
        self._qtd_helices = qtd_helices

    @property
    def qtd_helices(self):
        return self._qtd_helices

    @qtd_helices.setter
    def qtd_helices(self, qtd_helices):
        self.qtd_helices = qtd_helices

    def getInformacoes(self):  # reimplementa
        super().getInformacoes()
        print("Quantidade de Helices:", self.qtd_helices)


