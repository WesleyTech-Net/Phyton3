valores = list()

cont = 1
while len(valores) < 5:
    
    try:
        num = int(input(f"Digite o {cont}º valor: "))
        cont += 1
        valores.append(num)
    except ValueError:
        print("Valor inválido. Tente novamente")

print(f"Você digitou os valores: ", end ="")

for i in valores:
    print(f"{i}", end=" ")

ordenada = sorted(valores.copy())
print(f"\nLista ordenada: ", end=" ")
for pos in ordenada:
    print(f"{pos}", end=" ")
    