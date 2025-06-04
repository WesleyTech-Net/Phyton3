m1 = float(input('Primeira nota: '))
m2 = float(input('Segunda nota: '))
m3 = float(input('Terceira nota: '))
media = (m1 + m2 + m3) / 3

if media >= 7:
    print(f'Sua média é de {media:.1f} pontos.')
    print('Você está aprovado! PARABÉNS!')
else:
    print(f'Sua média é de {media:.1f} pontos.')
    print('Você está reprovado! ESTUDE MAIS!')