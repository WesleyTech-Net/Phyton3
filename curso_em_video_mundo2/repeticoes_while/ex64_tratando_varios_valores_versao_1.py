value = int(input("Digite um número (999 para parar): "))

soma = 0
cont = 0
while value != 999:
    cont += 1
    soma += value
    value = int(input("Digite um número (999 para parar): "))

print(f"Você digitou {cont} e a soma deles é igual a {soma}")