numeros_pares_impares = [[], []]

cont = 1
for i in range(1, 7 + 1):
    numeros_escolha = int(input(f"{i}º valor: "))
    cont += 1

    if numeros_escolha % 2 == 0:
        numeros_pares_impares[0].append(numeros_escolha)
    else:
        numeros_pares_impares[1].append(numeros_escolha)

print(f"Todos os valores: {numeros_pares_impares}")

numeros_pares_impares[0].sort()
print(f"Os valores pares foram {numeros_pares_impares[0]}")

numeros_pares_impares[1].sort()
print(f"Os valores ímpares foram {numeros_pares_impares[1]}")