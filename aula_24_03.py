from datetime import datetime
from datetime import date

nome = input("Digite o nome: ")
nascimento = input("Digite a data de nascimento: ")
idade = date.today().year - datetime.strptime(nascimento, '%d/%m/%Y').year

    if nome == "0" or "zero" and nascimento == "0" or "zero":
    print(nome, idade)
    print("FIM")
    while nome != "zero" or "0" and nascimento != "zero" or "0":
    return


