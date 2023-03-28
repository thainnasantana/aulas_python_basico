nome = ""
while nome != "zero" or "0" and nascimento != "zero" or "0":
    nome = input("Insira seu nome:" )
    nascimento = input("Insira sua data de nascimento:" )
    if nome == "0" or "zero" and nascimento == "0" or "zero":
        print(nome, nascimento)

print("FIM")

>>> from datetime import datetime
>>> data_nascimento = input('Digite a data de nascimento: ')
Digite a data de nascimento: 15/02/1982
>>> datetime.strptime(data_nascimento, '%d/%m/%Y')
datetime.datetime(1982, 2, 15, 0, 0)
--
from datetime import datetime
from datetime import date

nome = input('Digite o nome: ')
sobrenome = input('Digite o sobrenome: ')
nascimento = input('Digite a data de nascimento: ')

idade = date.today().year - datetime.strptime(nascimento, '%d/%m/%Y').year

print(f'Olá! O nome completo é {nome} {sobrenome} e hoje você tem {idade} anos')