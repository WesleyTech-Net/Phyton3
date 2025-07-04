tupla = (int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")))

print(f"Você inseriu os valores: ", end="")
for i in tupla:
    print(f'{i}', end=" ")