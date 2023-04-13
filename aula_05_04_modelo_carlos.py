
from datetime import date

hoje = date.today()
nome = input("nome: ")

while nome.lower() != "zero" and nome != "0":

    data_de_nascimento = input("data de nascimento: ").split('/')

    nascimento = {
        "ano": int(data_de_nascimento[2]),
        "dia":int(data_de_nascimento[0]),
        "mes":int(data_de_nascimento[1])
        }

    idade = int(hoje.year - nascimento["ano"])

    if hoje < date(hoje.year, nascimento["mes"], nascimento["dia"]):
    idade -= 1 
    print("-"*30)
    print(f"seu nome é {nome}, sua idade é {idade} , logo sua data se nacimento é {data_de_nascimento}")
    print("-"*30)

    nome = input("nome: ")

print('Fim!')