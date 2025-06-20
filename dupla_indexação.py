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


  
