class Pessoa:

    def __init__(self, nomeP = None, telefoneP = None):
        self.nome = nomeP
        self.telefone = telefoneP

    def imprimir(self):
        print("Nome: ", self.nome)
        print("Fone: ", self.telefone)