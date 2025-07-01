cont = soma = 0


while True:
    numero = int(input("Insira um número [999 para sair]: "))
    try:
        if numero == 999:
            break
        else:
            cont += 1
            soma += numero
            continue
    except ValueError:
        print("Valor inválido. Tente novamente...")

print(f"\nVocê insiriu {cont} número(s) e a soma entre eles é igual a {soma}.")        