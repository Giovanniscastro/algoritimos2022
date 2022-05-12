from Pessoa import Pessoa

class Fisica(Pessoa):
    
    def __init__(self, nomeF = None, telefoneF = None, cpfF = None):
        super().__init__(nomeF, telefoneF)
        self.cpf = cpfF
    
    def imprimir(self):
        super().imprimir()
        print( "CPF: ", self.cpf)