ano = int(input('Escolha um ano entre 1800 até 2025: '))
if ano % 4 == 0:
    print(f'O ano {ano} é um ano bissexto')
else:
    print(f'O ano {ano} não bissexto')