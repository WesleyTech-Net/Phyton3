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

#Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
numerador = int(input("Insira o numerador: "))
denominador = int(input("Insira o denominador (diferente de 0): "))

print(f"A divisão inteira entre {numerador} / {denominador} = {numerador // numerador}")

#Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
numerador = int(input("Insira o numerador: "))
denominador = int(input("Insira o denominador (diferente de 0): "))

print(f"O resto da divisão entre {numerador} / {denominador} = {numerador % numerador}")

#Crie um código que solicita 3 notas de um estudante e imprima a média das notas.
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média total é: {media}")

#Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.
v1 = 5
v2 = 12
v3 = 20
v4 = 15
media_ponderada = (v1 * 1 + v2 * 2 + v3 * 3 + v4 * 4) / (1 + 2 + 3 + 4)
print(f"Total da media ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4, é igual a: {media_ponderada}")