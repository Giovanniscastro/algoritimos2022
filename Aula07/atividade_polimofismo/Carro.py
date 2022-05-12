from Veiculo import Veiculo

class Carro( Veiculo ):

        def __init__(self, modelo, ano, portas):
                self.modelo = modelo
                self._ano = ano
                self.portas = portas

        @property
        def ano(self):
                return self._ano

        @ano.setter
        def ano(self, valor):
            self._ano = valor

        @property
        def modelo(self):
                return self._modelo

        @modelo.setter
        def modelo(self, valor):
            self._modelo = valor


        def imprimirEspecifico(self):
                print("Modelo: " , self.modelo )
                print("Ano: " , self.ano )
                print("Portas: " , self.portas )
        