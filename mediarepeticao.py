soma = 0
cont = 1
while (cont <=4):
    x = float(input(f'Insira a {cont}º nota: '))
    soma += x
    cont += 1
    media = soma /4
if (media >= 70):
    print(f'Sua nota foi {media:.2f}. VOCÊ ESTÁ APROVADO!')
else:
    print(f'Sua nota foi {media:.2f}. VOCÊ ESTÁ REPROVADO!')