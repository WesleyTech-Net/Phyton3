food = ["Laranja", "Lasanha", "Bacon", "Macarrão"]
print(food[0])

#dupla indexação
food = ["Laranja", "Lasanha", "Bacon", "Macarrão"]
print(food[0][0])
print(food[3][0])

#exemplo
food = ["Laranja", "Lasanha", "Bacon", "Macarrão"]
for item in food:
    for letra in item:
        print(letra, end='')
    print()

#exemplo com range
food = ["Laranja", "Lasanha", "Bacon", "Macarrão"]
for i in range(0,len(food), 1):
    for j in range(0, len(food[i]), 1):
        print(food[i][j], end = "")
    print("\n")

#Imagine uma situação que você deve realizar o cadastro de uma lista de compras em um sistema.
#Cada produto comprado deverá ser registrado com seu nome, quantidade e valor unitário.

item = []
mercado = []

for i in range(3):
    try:

        item.append(input('Digite o nome do item: '))
    except ValueError:
        print("Item inválido. Tente novamente...")
        continue
    item.append(int(input('Digite a quantidade: ')))
    item.append(float(input('Digite o valor: ')))
    mercado.append(item[:])
    item.clear()
print(mercado)
  