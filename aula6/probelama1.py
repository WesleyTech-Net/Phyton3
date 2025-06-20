#Escreva um algoritmo que crie uma tupla com 10 palavras. Encontre dentro dessa tupla as vogaais de cada palavra.
#Faça um print na tela com o nome da palavra e suas respectivas vogais

palavras = ('Avião', 'Banco', 'Sorte', 'Amor', 'Vida', 'Paralelepípedo', 'Intrínseco', 'Controle', 'Programação', 'Desenvolvedor')

for palavra in palavras:
    print(f'\nPalavra: {palavra.upper()}. Vogais: ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
