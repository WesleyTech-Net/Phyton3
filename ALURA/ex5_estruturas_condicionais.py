

#9) Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.

numero = input("Escolha um número: ")
valor = float(numero)

if valor.is_integer():
    print(f"O número {numero} é um inteiro")
else:
    print(f"O número {numero} é decimal")