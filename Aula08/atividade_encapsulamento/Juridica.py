from Pessoa import Pessoa

class Juridica( Pessoa ):
    def __init__(self, nomeJ = None, telefoneJ = None, cnpjJ = None):
        super().__init__(nomeJ, telefoneJ)
        self.cnpj = cnpjJ
    
    def imprimir(self):
        print("Razão Social: ", self.nome)
        print("Telefone: ", self.telefone)
        print( "CNPJ: ", self.cnpj)