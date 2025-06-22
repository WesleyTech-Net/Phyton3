from datetime import date

anoNascimento = int(input("Qual o seu ano de nascimento? "))
atual = date.today().year
idade = atual - anoNascimento


print("Você tem", idade, "anos de idade!")

if idade == 18:
    print(f"Você tem {idade} anos de idade, está na hora de se alistar.")
elif idade > 18:
    idadePassou = idade - 18
    print(f"Você tem {idade} anos de idade, já passou {idadePassou} anos do período de alistamento.")
else:
    idadeFalta = 18 - idade
    print(f"Você tem {idade} anos de idade, ainda falta {idadeFalta} anos para se alistar.")