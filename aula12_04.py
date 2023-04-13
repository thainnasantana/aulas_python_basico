from datetime import datetime, date

nome = input("Digite o nome: ")

while nome != "zero" and nome != "0":
    nascimento = input("Digite a data de nascimento: ")
    if len(nascimento) != 10:
        print("Formato Inválido! Digite com DD/MM/AAAA")
        continue
    
    for caracter in nascimento:
        if caracter not in '0123456789/':
            print("Formado Inválido! Insira números válidos em DD/MM/AAAA")
            break 
    
    data_de_nascimento = data_de_nascimento.split('/')
    print(data_de_nascimento)
    nascimento = {
        "dia":int(data_de_nascimento[0]),
        "mes":int(data_de_nascimento[1]),
        "ano": int(data_de_nascimento[2])
        }
    
    if nascimento["dia"] <= 31 and nascimento["mes"] <= 12 and nascimento["ano"] >= 1910 <= date.today():
        print("FIM")