from abc import ABCMeta, abstractmethod, abstractproperty

class Veiculo(metaclass=ABCMeta):

        @property
        
        def modelo(self):
                pass
        
        @modelo.setter
        @abstractmethod
        def modelo(self, valor):
                pass


        @property
        def ano(self):
                pass
        
        @ano.setter
        @abstractmethod
        def ano(self, valor):
            pass

        def imprimir(self):
            print("Modelo: " , self.modelo )
            print("Ano: " , self.ano )

        @abstractmethod
        def imprimirEspecifico(self):
            pass
        

