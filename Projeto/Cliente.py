#Utilizamos a palavra reservada pass, quando nenhuma estrutura será definida no corpo dessa classe.
#A palavra def é utilizada para a declaração de método.
#Para definir o construtor adicionamos: underline, underline, a palavra reservada init, underline, underline. 
#O init() é um método especial que será chamado sempre que criarmos um objeto da classe.
#Incluímos o parâmetro obrigatório self, que está presente em todos os métodos. Resumidamente, podemos afirmar que o parâmetro self, neste momento, exporta as características do objeto.
#Com o parâmetro self são passados os parâmetros que serão utilizados para inicialização dos atributos.
#Para definir o método public é necessário o uso do underline ”_” na frente do nome.
#Para definir o método protected adicione um underline ”_” antes do nome.
#Para definir o método private adicionamos underline duplo ”__” na frente do nome.

class Cliente:
    def __init__(self, n, fone):
        self._nome = n
        self._telefone = fone

#método get
def get_nome(self):
    return self._nome

#método set
def set_nome(self, nome):
    self._nome = nome

        
    

