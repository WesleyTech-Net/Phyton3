numeros = "zero", "one", "two", "three", "four", "five", "six", "seven", "eigth", "nine", "ten"

escolha = int(input("Digite um numero entre 0 e 10:"))

while escolha > 10 or escolha < 0:
    print("Tente novamente.", end=" ")
    escolha = int(input("Digite um numero entre 0 e 10: "))

for cont in range(0, len(numeros)+1):
    if 0 <= escolha <= 10:
        print(f"O número {escolha} por extenso é: {numeros[escolha]}")
    else:
        print("Número fora do intervalo permitido. Digite de 0 a 10.")