from random import randint
from time import sleep

print(f"{'GERAR TOKEN':=^45}")

tokens = []
for i in range(1000, 9999):
    tokens.append(i)


while True:

    try:
        opcao = str(input("Deseja gerar um token (S/N): ")).strip().upper()[0]

        if opcao == "N":
            break

    except ValueError:
        print("Opção inválida. Tente novamente...")
