#A classe Main não possui atributos. Utilizamos apenas a palavra reservada pass.
class Main:
    pass

#importação da classe Cliente
from Cliente import Cliente

#importação da classe Conta
from Conta import Conta

#instanciação de um novo objeto
c1 = Cliente("Letícia", "1199999-9999")
conta = Conta(c1._nome, 3101, 0)

#impressão do resultado
print(c1)
print(c1._nome, "e", c1._telefone)
print(conta.titular, "Número:", conta.numero, "Saldo =", conta.saldo)