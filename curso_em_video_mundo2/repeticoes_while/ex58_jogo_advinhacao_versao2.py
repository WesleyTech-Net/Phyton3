from time import sleep
from random import randint
print(10 * "=")
print("JOGO DA ADVINHAÇÃO")
print(10 * "=")
nome = str(input("Qual o seu nome: ")).strip().upper()
print(f"Vou pensar em um número {nome}. Tente advinhar...")
sleep(2)
cont = 0


while True:
    try:

        jogador = int(input("Em que número eu pensei (0 até 5)? "))
        computador = randint(0, 5)
        print("Processando...")
        sleep(2)

        if jogador == computador:
            cont += 1
            print(f"Eu pensei no número {computador}. PARABÉNS VOCÊ ACERTOU!")
            print(f"No total foram {cont} jogadas.")
            escolha = str(input("Deseja jogar novamente (S/N): ")).strip()
            
            if escolha in "Ss":
                continue
            elif escolha in "Nn":
                print(f"OBRIGADO POR JOGAR COMIGO {nome}!")
                break
        else:
            cont += 1
            print(f"Eu pensei no número {computador}. Você ERROU! Tente novamente...")
            continue

    except ValueError:
        print("Opção inválida. Tente novamente...")
        continue


