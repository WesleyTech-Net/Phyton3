print(10 * '-', 'ESCOLHA O LADO', 10 * '-')
print('1 - NORTE', '\n2 - SUL', '\n3 - LESTE', '\n4 - OESTE')
escolha = int(input('Escoolha um lado de 1 a 4: '))
if escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4:
    print(f'O lado escolhido foi{escolha} VOCÊ ESCAPOU!')