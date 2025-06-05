print(10 * '-' + 'ESCOLHA A FRUTA' + 10 * '-','\n1 - MAÇA', '\n2 - LARANJA', '\n3 - BANANA\n' + 35 * '-')
escolha = int(input('Qual sua escolha: '))
kilo = float(input('Insira o peso: '))

if escolha == 1:
    print(f'O peso do produto é {kilo}kg. Total a pagar: R$ {kilo * 2.30}')
elif escolha == 2:
    print(f'O peso do produto é {kilo}kg. Total a pagar: R$ {kilo * 3.60}')
elif escolha == 3:
    print(f'O peso do produto é {kilo}kg. Total a pagar: R$ {kilo * 1.85}')
else:
    print('PRODUTO INEXISTENTE')