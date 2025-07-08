#Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

print(f"A soma de {n1} + {n2} = {n1 + n2}")

#Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.
n1 = int(input("\nPrimeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))

print(f"A soma de {n1} + {n2} + {n3} = {n1 + n2 + n3}")

#Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.
n1 = int(input("\nPrimeiro valor: "))
n2 = int(input("Segundo valor: "))

print(f"A subtrção de {n1} - {n2} = {n1 - n2}")

#Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.
n1 = int(input("\nPrimeiro valor: "))
n2 = int(input("Segundo valor: "))

print(f"A multiplicação de {n1} x {n2} = {n1 * n2}")

#Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
numerador = int(input("Insira o numerador: "))
denominador = int(input("Insira o denominador (diferente de 0): "))

print(f"A divisão de {numerador} / {denominador} = {numerador / numerador}")

#Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.
operador = int(input("Valor para o operador: "))
potencia = int(input("Valor para potência: "))
exponeciacao = operador ** potencia
print(f"A exponenciação entre {operador} e {potencia} é igual a: {exponeciacao}")