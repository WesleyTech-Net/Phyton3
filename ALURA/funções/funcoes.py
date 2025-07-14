#1) Escreva um código que lê a lista abaixo e faça:
#lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
#A leitura do tamanho da lista
#A leitura do maior e menor valor
#A soma dos valores da lista

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

tamanho = len(lista)
maior = max(lista)
menor = min(lista)
soma = sum(lista)
print(f"A lista possui {tamanho} números em que o maior é {maior} e o menor número é {menor}")
print(f"A soma dos valores presentes na lista é igual a {soma}")

#2) Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, 
# de acordo com a escolha da pessoa usuária. Como exemplo, para o número 7, 
# a tabuada deve ser mostrada no seguinte formato:
def tabuada(numero):
    for i in range(1, 11):
        print(f"{i} x {numero} = {i * numero}")

print("Tabuada do: ", end="")
op = int(input())

tabuada(op)#o parâmetro "op" irá utilizar o número escolhido no input que por sua vez colcoará esse valor dentro do parÂmetor da função.

#3) Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:
#[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

def encontrar_multiplos_3(lista):
    return list(filter(lambda x: x % 3 == 0, lista))

numeros = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
lista_multiplos_3 = encontrar_multiplos_3(numeros)


print(f"Os Múltiplos de 3 são: ", end="")
for i in lista_multiplos_3:
    print(i, end=" ")

#4) Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. 
# Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.
def quadrado_numeros(lista):
    return list(map(lambda x: x ** 2, lista))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_quadrado_numeros = quadrado_numeros(numeros)
print("O quadrado de cada número é: ")

for num, quadrado in zip(numeros, lista_quadrado_numeros):# zip() é uma função embutida do Python que serve para juntar elementos de duas (ou mais) listas em pares.
    print(f"{num}² = {quadrado}")