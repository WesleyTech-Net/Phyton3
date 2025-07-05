valores = list()
par = list()
impar = list()

OP = ("S", "N")
cont = 1
while True:

    try:

        num = int(input(f"Digite o {cont}º número: "))
        cont += 1
        valores.append(num)

    except ValueError:
        print("❌ Opção inválida. Tente novamente...")
    
    while True:
        escolha = str(input("Quer continuar (S/N): ")).strip().upper()[0]
        if escolha in OP:
            break
        else:
            ("❌ Opção Inválida. Digite Sim ou Não")
    if escolha == "N":
        break

print("FIM DO PROGRAMA")

print("A lista completa: ", end=" ")
for i in valores:
    print(f"{i}", end=", ")

for i in valores:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print("\n🟢 Lista dos valores pares: ", end="")
for i in par:
    print(f"{i}", end=", ")

print("\n🔴 Lista dos valores impares: ", end="")
for i in impar:
    print(f"{i}", end=", ")