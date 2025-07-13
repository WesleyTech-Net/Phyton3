#1) Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de
#papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08].
#Com esses valores, faça um programa que calcule a média de gastos. Dica: use as funções built-in
#sum() e len().

valores_gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

media_gastos = sum(valores_gastos) / len(valores_gastos)
print(f"Média de gastos da empresa: R$ {media_gastos:.2f}")

#2) Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de
#3000 reais e calcule a porcentagem quanto ao total de compras.

acima_300 = len([valores for valores in valores_gastos if valores > 3000])
print(f"Total de gastos acima de R$3.000,00: {acima_300}")
total_compras = len(valores_gastos)
porcentagem = (acima_300 / total_compras) * 100

print(f"Isso representa {porcentagem:.2f}% do total de compras.")

#3)Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].

lista = list()

for i in range(1, 6):
    numeros = int(input(f"{i}º valor: "))
    lista.append(numeros)

print(lista)

#4) Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.
lista = list()

for i in range(1, 6):
    numeros = int(input(f"{i}º valor: "))
    lista.append(numeros)

print(sorted(lista, reverse = True))

#5) Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.
lista_numeros = []

primos = []

op = int(input("Escolha um número: "))
cont = 1

for i in range(1, op + 1):
    lista_numeros.append(cont)
    cont += 1

for numeros_primos in lista_numeros: #verifica os números dentro da lista_numeros e separa apenas os números primos
    if numeros_primos > 1:
        e_primo = True
        for i in range(2, int(numeros_primos ** 0.5) + 1):
            if numeros_primos % i == 0:
                e_primo = False
                break
        if e_primo:
            primos.append(numeros_primos)

print(f"Esses são os números primos entre 1 e {op}: ", end=" ")
for i in primos:
    print(f"{i}", end=" ")

#6) Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.
import datetime

dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))

try:

    data = datetime.date(ano, mes, dia)
    print(f"A data {data.strftime('%d/%m/%Y')} é uma data válida para análise.")#ordem para Brasil

except ValueError:
    print("Data inválida.")