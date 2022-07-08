"""
Construa um software em Python que implemente uma Pilha de carros e uma Pilha de drones.

As classes carro e drone herdam da classe veículo os atributos e comuns às duas classes.

A classe carro é composta dos atributos marca, modelo e portas. O atributo portas é fracamente privado.

A classe drone é composta dos atributos marca, modelo e quantidade de hélices. O atributo quantidade de hélices é fortemente privado.

Todas classes devem ter um método para imprimir as informações dos seus respectivos atributos.

Implemente uma tela com um menu (funcionando) que permita ao usuário:

-> Adicionar e remover carros da Pilha.

-> Adicionar e remover drones da Pilha.

-> Imprimir a Pilha de carros e a Pilha de drones.

Pode ser entregue um zip com os arquivos ou o link do repositório no GitHub contendo o código desenvolvido
"""

from Drone import Drone
from Carro import Carro


def menu():
    print('''O que você deseja fazer:
           0 -  Sair
           1 -	Adicionar Drone
           2 -	Adicionar Carro
           3 -	Remover Drone
           4 -	Remover Carro
           5 -	Imprimir Drones
           6 -	Imprimir Carros
           Escolha: '''
          )
    print()
    print()
    return input()


lista_Drone = []
lista_Carro = []

while True:

    resposta = menu()

    if resposta == "0":
        break

    elif resposta == "1":
        print("Adicionando o Drone: ")
        marcaD = input("Marca: ")
        modeloD = input("Modelo: ")
        qtd_helicesD = int(input("Quantidade de Helices: "))
        d1 = Drone(marcaD, modeloD, qtd_helicesD)
        lista_Drone.append(d1)
        print("Drone adicionado com sucesso.")

    elif resposta == "2":
        print("Adicionando o Carro: ")
        marcaC = input("Marca: ")
        modeloC = input("Modelo: ")
        qtd_portasC = int(input("Quantidade de Portas: "))
        c1 = Carro(marcaC, modeloC, qtd_portasC)
        lista_Carro.append(c1)
        print("Carro adicionado com sucesso.")


    elif resposta == "3":
        print("Removendo o Drone: ")
        modeloD = input("Modelo: ")
        existe_modelo = False
        for drone in lista_Drone:
            if drone.modelo == modeloD:
                existe_modelo = True
                lista_Drone.remove(drone)
                print("Drone removido com sucesso.")

        if not existe_modelo:
            print("Modelo de drone não encontrado")

    elif resposta == "4":
        print("Removendo o Carro: ")
        modeloC = input("Modelo: ")
        existe_modelo = False
        for carro in lista_Carro:
            if carro.modelo == modeloC:
                existe_modelo = True
                lista_Carro.remove(carro)
                print("Carro removido com sucesso.")

        if not existe_modelo:
            print("Modelo de carro não encontrado")


    elif resposta == "5":
        print("As informações dos Drones são: ")
        for drone in lista_Drone:
            drone.getInformacoes()

    elif resposta == "6":
        print("As informações dos Carros são: ")
        for carro in lista_Carro:
            carro.getInformacoes()

    else:
        print("Erro. Favor digitar apenas alguma das opções do menu!")