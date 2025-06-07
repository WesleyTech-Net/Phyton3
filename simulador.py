print(10 * '-', 'SIMULADOR', 10 * '-')
qtd = float(input('Insira o kWh consumida: '))
print('Qual o tipo de instalação? ')
print('R - RESIDÊNCIA', '\nI - INDUSTRIA', '\nC - COMÉRCIO')

escolha = input('Escolha o tipo de instalação: ')
if escolha == 'R' or escolha == 'r' and qtd <= 500:
    print(f'Essa unidade consumiu o valor total de R$ {qtd * 0.40}')
elif escolha == 'R' or escolha == 'r' and qtd > 500:
    print(f'Essa unidade consumiu o valor total de R$ {qtd * 0.65}')
elif escolha == 'C' or escolha == 'c' and qtd <= 1000:
    print(f'Essa unidade consumiu o valor total de R$ {qtd * 0.55}')
elif escolha == 'C' or escolha == 'c' and qtd > 1000:
    print(f'Essa unidade consumiu o valor total de R$ {qtd * 0.60}')
elif escolha == 'I' or escolha == 'i' and qtd <= 5000:
    print(f'Essa unidade consumiu o valor total de R$ {qtd * 0.55}')
elif escolha == 'I' or escolha == 'i' and qtd > 5000:
    print(f'Essa unidade consumiu o valor total de R$ {qtd * 0.60}')
else:
    print('OPÇÃO INCORRETA! TENTE OUTRA VEZ...')