pessoas = list()
dado = list()
cont = 1
cont2 = 0
maior_peso = menor_peso = 0
while True:

    print(f"{cont}º pessoa")
    cont += 1
    try:

        dado.append(str(input("Nome: ").strip()))
        dado.append(float(input("Peso: ")))

        if len(pessoas) == 0:
            maior_peso = menor_peso = dado[1]
        else:
            if dado[1] > maior_peso:
                maior_peso = dado[1]
            if dado[1] < menor_peso:
                menor_peso = dado [1]

        print("Dado cadastrado com sucesso...")
        pessoas.append(dado[:])
        dado.clear()
        cont2 += 1

        op = str(input("Quer cadastrar outra pessoa (S/N)? ")).strip().upper()[0]
        if op in "S":
            continue
        elif op in "N":
            break

    except ValueError:
        print("❌ Valor inválido tente novamente...")

print(f"Total de pessoas cadastradas: {cont2}")
print(f"O maior peso foi de {maior_peso} kg.", end=" ")

for i in pessoas:
    if i[1] == maior_peso:
        print(f"Peso de {i[0]}")

print(f"O menor peso foi de {menor_peso} kg")
for i in pessoas:
    if i[1] == menor_peso:
        print(f"Peso de {i[0]}")



