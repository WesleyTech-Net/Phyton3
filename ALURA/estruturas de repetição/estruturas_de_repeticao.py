#1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
numero1 = int(input("Primeiro valor: "))
numero2 = int(input("Segundo valor: "))

for i in range(numero1, numero2 + 1):
    print(f"{i}")

#2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.
colonia_a = 4
colonia_b = 10

dias = 0

while colonia_a < colonia_b:
    colonia_a *= 1.03
    colonia_b *= 1.015
    dias += 1
print(f"A colonia A ultrapssou ou igualou a colonia B em {dias} dias")

#3) Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da
#empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai
#receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma
#nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.

for i in range(1, 16):

    while True:
        try:

            dados = int(input(f"{i}º nota entre 0 e 5: "))
            if 0 <= dados <= 5:
                break
            else:
                print("Opção Inválida. Tente novamente...")

        except ValueError:
            print("Entrada não numérica. Tente novamente...")

print("OBRIGADO PELAS NOTAS!")


#4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. 
# A leitura deve ser encerrada ao ser enviado o valor -273°C.

soma = 0
cont = 0

while True:
    try:
        temperaturas = int(input("Insira a temperatura (para sair digite -273): "))
        if temperaturas == -273:
            break

        soma += temperaturas
        cont += 1
    except ValueError:
        print("Valor não numérico inserido. tente novamente")


if cont > 0:
    media = soma / cont
    print(f"Você adicionou {cont} temperaturas. A média entre elas é igual a {media:.2f}.")
else:
    print("Nenhuma temperatura foi inserida.")

#5) Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. Lembrando que o fatorial de um número inteiro é a 
# multiplicação desse número por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.
numero = int(input("Escolha um número para fatorar: "))

fatorial = 1
for i in range(numero, 0, - 1):
    print(i, end = ' ')
    if i != 1:
        print("x ", end='')
    fatorial *= i
print(f"= {fatorial}")


