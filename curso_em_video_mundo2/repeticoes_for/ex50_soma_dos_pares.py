soma = 0
cont = 0
for i in range(1, 6 + 1):
    num = int(input(f"{i}º número: "))
    if num % 2 == 0: 
        soma += num
        cont += 1
print(f"Você informou {cont} números pares e a soma entre eles é igual a {soma}")