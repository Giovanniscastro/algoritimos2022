#from ContaBancaria import ContaBancaria
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

'''cb = ContaBancaria()
cb.Depositar()
print("---------------")
cb.Cadastrar()'''

cc = ContaCorrente("1151A", 178941, 12)
cc.Depositar()
cc.DepositarEspecifico()
print("---------------")
cc.Cadastrar()
cc.CadastrarEspecifico()


cp = ContaPoupanca("1148B", 178941, 13)
cp.Depositar()
cp.DepositarEspecifico()
print("---------------")
cp.Cadastrar()
cp.CadastrarEspecifico()

#conta bancaria deu erro