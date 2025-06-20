game = {}
games = []

for i in range(3):
    game['Nome'] = input('Nome do jogo: ')
    game['Console'] = input('Foi lançado para qual console? ')
    game['Ano de Lançamento'] = int(input('Ano de lançamento: '))
    games.append(game.copy())
print(20 * '-')
for jogos in games:
    for chave, valor in jogos.items():
        print(f'{chave} : {valor}.')