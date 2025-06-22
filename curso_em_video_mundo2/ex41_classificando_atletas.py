from datetime import date

ano =  int(input("Ano de nascimento: "))
atual = date.today().year
idade = atual - ano
print(f"Esse atleta tem {idade}")

if idade < 9:
    print("Classificação: MIRIM")

elif 9 <= idade <= 14:
    print("Classificação: INFANTIL")

elif 14 < idade <= 19:
    print("Classificação: JÚNIOR")

elif 19 < idade <= 25:
    print("Classificação: SÊNIOR")

else:
    print("Classificação: MASTER")