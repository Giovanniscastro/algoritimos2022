from Veiculo import Veiculo

class Bicicleta( Veiculo ):

        def __init__(self, modelo, ano,num_marchas, bagageiro):
                self._modelo = modelo
                self._ano = ano
                self._num_marchas = num_marchas
                self._bagageiro = bagageiro

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
        
        @property
        def num_marchas(self):
                return self._num_marchas

        @num_marchas.setter
        def num_marchas(self, valor):
                self._num_marchas = valor
        
        @property
        def bagageiro(self):
                return self._bagageiro

        @bagageiro.setter
        def bagageiro(self, valor):
                self._bagageiro = valor

        def imprimir(self):
                print("Bicicleta:")
                super().imprimir()
        
        def imprimirEspecifico(self):
                self.imprimir()
                print( "num_marcha: " , self.num_marchas)