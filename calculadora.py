print(10 * '-', 'CALCULADORA', 10 * '-')
v1 = float(input('Insira um valor: '))
v2 = float(input('Insira outro valor: '))
print(35 * '-')
print('1 - ADIÇÃO', '\n2 - SUBTRAÇÃO', '\n3 - MULTIPLICAÇÃO', '\n4 - DIVISÃO', '\n5 - Para sair.')
escolha = int(input('Qual operação deseja utilizar? '))

if escolha == 1:
    print(f'A soma de {v1} + {v2} = {v1 + v2}')
elif escolha == 2:
    print(f'A subtração de {v1} - {v2} = {v1 - v2}')
elif escolha == 3:
    print(f'A multiplicação de {v1} x {v2} = {v1 * v2}')
elif escolha == 4:
    print(f'A divisão de {v1} / {v2} = {v1 // v2}')
elif escolha == 5:
    print('MUITO OBRIGADO! ATÉ LOGO!')
else:
    print('OPÇÃO INCORRETA! TENTE OUTRA VEZ...')