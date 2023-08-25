#A classe Main não possui atributos. Utilizamos apenas a palavra reservada pass.
class Main:
    pass

#importação da classe Cliente
from Cliente import Cliente

#instanciação de um novo objeto
c1 = Cliente("Letícia", "1199999-9999")

#impressão do resultado
print(c1)
print(c1.nome, "e", c1.telefone)