#Em Python, Classe é um tipo de dado. Todo valor pertence a uma classe, por ex.: "Oi" pertence a classe string(stg).

class Pessoa(): #As classes precisam começar com a nomeclatura de letra maíscula
  
    def __init__(self, nome="", nascimento=""): #O __init__ é o construtor da classe, utilizado para inicializar atributos.
        self.nome = nome
        self.nascimento = nascimento


    def andar (self): #Self é uma variável que referencia um determinado objeto da classe. Todo método de uma classe recebe self como promeiro parâmetro.
        print(self.nome)
        print(self.nascimento)

var = Pessoa(nome=input(), nascimento=input()) #Instanciar é atribuir ao objeto (variável) uma instância. INSTANCIA ANTES DE UTILIZAR.
print(var.nome)
print(var.nascimento)
var.andar
