soma = 0
cont = 1
while (cont <=4):
    x = int(input(f'Insira a {cont}º nota: '))
    soma += x
    cont += 1
    media = soma /4
if (x >= 70):
    print(f'Sua nota foi {media}. VOCÊ ESTÁ APROVADO')
else:
    print(f'Sua nota foi {media}. VOCÊ ESTÁ REPROVADO')