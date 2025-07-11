


#4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. 
# A leitura deve ser encerrada ao ser enviado o valor -273°C.

temperaturas = int(input("Insira a temperatura (para sair digite -273): "))

soma = 0
cont = 0
while temperaturas != 273:

    temperaturas = int(input("Insira a temperatura (para sair digite -273): "))

    cont += 1
    soma += temperaturas
    media = soma / cont

print(f"Você adicionou {cont} temperaturas. A média entre elas é igual a {media:.2f}.")

