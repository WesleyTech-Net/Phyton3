print(10 * '-', 'EMPRÉSTIMO BANCÁRIO', 10 * '-')
salario = float(input('Qual o seu salário líquido total? '))
casa = float(input('Qual o valor da casa desejada? '))
anos = int(input('Deseja pagar em quantos anos? '))

prestacao = casa / (anos * 12)
min = salario * 30 / 100

print(f'Para pagar uma casa de R${casa} em {anos} anos, a prestação será de R$ {prestacao:.2f}')

if prestacao <= min:
    print('EMPRÉSTIMO APROVADO!')
else:
    print('EMPRÉSTIMO NEGADO')