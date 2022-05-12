from Veiculo import Veiculo
from Carro import Carro
from Moto import Moto
from biciclieta import Bicicleta
c1 = Carro("Doblo", 2005, 4)
c1.imprimir()
c1.imprimirEspecifico()


m1 = Moto("Titan", 2010, 150)
m1.imprimir()
print("--------------")
m1.imprimirEspecifico()

b1 = Bicicleta("BMX", 2005, 6, None)
b1.imprimir()
print("--------------")
b1.imprimirEspecifico()

