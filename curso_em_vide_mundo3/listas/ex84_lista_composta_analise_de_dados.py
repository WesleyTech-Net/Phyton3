pessoas = list()
dado = list()
cont = 1
cont2 = 0
while True:

    print(f"{cont}º pessoa")
    cont += 1
    try:

        dado.append(str(input("Nome: ").strip()))
        dado.append(float(input("Peso: ")))
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




