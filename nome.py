nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

if nome == 'Wesley':
    print('Olá Wesley!')
elif idade < 18:
    print('Você não é Wesley! E ainda por cima é menor de 18 anos.')
elif idade > 100:
    print('VOCÊ NÃO É IMORTAL!')
