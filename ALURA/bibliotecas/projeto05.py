from math import pi, pow 

raio = float(input("Digite o raio da área circular em metros: "))


area = pi * pow(raio, 2)

preco_grama = 25

valor = area*preco_grama

print(f"O preço total é R${round(valor, 2)} para uma área de {round(area, 2)} metros de grama")
