#1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
numero1 = int(input("Primeiro valor: "))
numero2 = int(input("Segundo valor: "))

for i in range(numero1, numero2 + 1):
    print(f"{i}")