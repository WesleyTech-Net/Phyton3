from random import choice
import time
print(10 * '-', 'JOGO DA MATEMÁTICA COM DESENHO', 10 * '-')
escolha = float(input('Escolha um número: '))
desenhos = ['Castelo', 'Carro', 'Bicicleta', 'Caminhão']
print('ESTOU ESCOLHENDO O SEU DESENHO...')
time.sleep(3)
print(f'VOCÊ TEM QUE DESENHAR {choice(desenhos)}')

if escolha % 2 == 0:
    print(f'E número {escolha} é par.')
    print('Desenha um quadrado')
    print('Pinte o quadrado de azul.')
else:
    print(f'O número {escolha} é impar.')
    print('Desenhe um triângulo')
    print('Pinte o triângulo de vermelho.')

print(10 * '-', 'VAMOS SOMAR!', 10 * '-')
n1 = int(input('Preciso de um número: ')) 
n2 = int(input('Preciso de outro número: '))

if (n1 + n2) % 2 == 0:
    print('A soma deu um número par.\n Desenhe um círculo!')
    print('Pinte o círculo com a verde.')
else:
    print('Desenhe um retângulo.')
    print('Pinte o retÇangulo de amarelo.')