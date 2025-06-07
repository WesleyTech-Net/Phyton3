soma = 0
cont = 1
while (cont <= 4):
    x = float(input(f'Insira a {cont}º nota: '))
    soma = soma + x
    cont = cont + 1
media = soma / 4
if media >= 70:
    print(f'Média final: {media:.2f}. Você está APROVADO!')
else:
    print(f'Média final: {media:.2f}. Você está REPROVADO!')