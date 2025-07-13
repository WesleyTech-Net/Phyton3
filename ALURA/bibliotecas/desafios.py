
#3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.
from random import choice
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

print(choice(lista))

#4. Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100.
from random import randrange
numero_sorteado = randrange(0, 100)
print(f"O número sorteado foi {numero_sorteado}")

#5. Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a
#potência do 1º número elevado ao 2º.
from math import pow
numero1 = int(input("Primeiro valor inteiro: "))
numero2 = int(input("Segundo valor inteiro: "))

resultado = pow(numero1, numero2)
print(f"O número {numero1} elevado ao {numero2} é igual a {int(resultado)}.")
