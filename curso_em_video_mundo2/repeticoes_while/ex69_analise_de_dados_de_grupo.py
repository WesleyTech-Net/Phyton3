contador_18 = 0
homem = 0
mulher_menor = 0

while True:
    print(10 * "-=")
    print("CADASTRE UMA PESSOA")
    print(10 * "-=")

    idade = int(input("Idade: "))
    if idade >= 18:
        contador_18 += 1

    sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    if sexo in "M":
        homem += 1
    elif sexo in "F" and idade < 20:
        mulher_menor += 1

    op = str(input("Quer continuar [S/N]: ")).strip().upper()[0]

    if op in "S":

        continue
    elif op in "N":
        break

print(f"\nTotal de pessoas com mais de 18 anos: {contador_18}")
print(f"Ao todo temos {homem} homem(ens) cadastrado(s)")
print(f"E temos {mulher_menor} mulher(s) com menos de 20 anos.")
