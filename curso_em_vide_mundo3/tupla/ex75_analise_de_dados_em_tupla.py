tupla = (int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")))

print(f"Você inseriu os valores: ", end="")
for i in tupla:
    print(f'{i}', end=" ")

print("\nOs valores pares digitados são: ", end=" ")
for pares in tupla:
    if pares % 2 == 0:
        print(pares, end=" ")

print(f"\nO valor 5 apareceu {tupla.count(5)} vezes.")

if 2 in tupla:
    print(f"O valor 2 está na posição {tupla.index(2) + 1}")
else:
    print("O valor 2 não foi encontrado em nunhuma posição!")
