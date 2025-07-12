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