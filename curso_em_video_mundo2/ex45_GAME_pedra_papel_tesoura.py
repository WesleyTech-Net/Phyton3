import random
import time

try:
    op1 = input("VAMOS JOGAR (S/N)? ").strip().upper()
    if op1 == 'S':
        print("""Escolha sua opção:
                [0] - PEDRA
                [1] - PAPEL
                [2] - TESOURA
                """)
        jogador = int(input("Qual sua Jogada? "))
        itens = ['PEDRA', 'PAPEL', 'TESOURA']
        computador = random.randint(0, 2)

        print("JO")
        time.sleep(1)
        print("KEN")
        time.sleep(1)
        print("PÔ!!")

        print(15 * "=-")
        print("O jogador escolheu {}".format(itens[jogador])) 
        print("O computador escolheu {}".format(itens[computador]))
        print(15 * "=-")

        if computador == 0: #COMPUTADOR JOGOU PEDRA
            if jogador == 0:
                print("EMPATE!")
            if jogador == 1:
                print("JOGADOR GANHOU!")
            elif jogador == 2:
                print("COMPUTADOR GANHOU!")

        elif computador == 1: #COMPUTADOR JOGOU PAPEL
            if jogador == 1:
                print("EMPATE!")
            if jogador == 2:
                print("JOGADOR GANHOU!")
            elif jogador == 0:
                print("COMPUTADOR GANHOU!")

        elif computador == 2: #COMPUTADOR JOGOU TESOURA
            if jogador == 2:
                print("EMPATE!")
            if jogador == 0:
                print("JOGADOR GANHOU!")
            elif jogador == 1:
                print("COMPUTADOR GANHOU!")

    elif op1 == 'N':
        print("MUITO OBRIGADO!")     
    else:
        print("OPÇÃO INVÁLIDA. Tente novamente...")
            
except ValueError:
    print("OPÇÃO INVÁLIDA. Tente novamente...")

       