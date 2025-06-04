print(10 * '-', 'ESCOLHA O QUE DESEJA COMPRAR', 10 * '-', '\n1 - Maça\n', '2 - Laranja\n', '3 - Banana' )

escolha = int(input('Qual sua escolha: '))
kilo = float(input('Insira o peso: '))
print(50 * '-')
if escolha == 1:
    print(f'Você comprou {kilo} kg de Maça. O preço total é de R$ {kilo * 2.30}')
else:
    if escolha == 2:
        print(f'Você comprou {kilo} Kg de Laranja. O preço total é de R$ {kilo * 3.60}')
    else:
        if escolha == 3:
            print(f'Você comprou {kilo} Kg de Banana. O preoõ total é de R$ {kilo * 1.85}')
        else:
            print('PRODUTO INEXISTENTE')