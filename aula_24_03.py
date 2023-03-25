#nf = int(input())
#nh = float(input())
#vh = float(input())
#print("NUMBER =",nf)
#print("SALARY = U$",(nh*vh))

nome = ""
while nome != "zero" or "0" and nascimento != "zero" or "0":
    nome = input("Insira seu nome:" )
    nascimento = input("Insira sua data de nascimento:" )
    if nome == "0" or "zero" and nascimento == "0" or "zero":
        print(nome, nascimento)

print("FIM")