from datetime import datetime, date

nome = input("Digite o nome: ")

while nome != "zero" and nome != "0":
    nascimento = input("Digite a data de nascimento: ")
    idade = date.today().year - datetime.strptime(nascimento, '%d/%m/%Y').year
    
    print(nome, idade)
    
    nome = input("Digite o nome: ")
