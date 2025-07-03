from random import randint

cont = 0
while True:

    jogador = int(input("Escolha um número: "))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = str(input("Par ou Ímpar? ")).strip().upper()[0]
    print(f"Você jogou {jogador} o computador jogou {computador}. Total deu {total}")

    if tipo == "P":
        if total % 2 == 0:
            cont = 0
            print("VOCÊ VENCEU!")
        else:
            print("VOCÊ PERDEU")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("VOCÊ VENCEU!")
        else:
            print("VOCÊ PERDEU")
            break