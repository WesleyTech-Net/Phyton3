from random import choice
from time import sleep

print(f"{'GERAR TOKEN':=^45}")

tokens = []
for i in range(1000, 9999):
    tokens.append(i)
    
tokens_pares = [t for t in tokens if t % 2 == 0]

while True:
    
    if not tokens_pares:
        break 

    try:
        opcao = str(input("Deseja gerar um token (S/N): ")).strip().upper()[0]

        if opcao == "N":
            break

        elif opcao == "S":
            #gera a escolha do token
            gerando = choice(tokens_pares)
            tokens_pares.remove(gerando)#remove os itens da lista para não repetir os mesmos números
            print("Gerando...")
            sleep(2)
            print(f"TOKEN: {gerando}")
            print("Expira em: ", end="")


            #faz uma contagem regressiva para inutilizar o token
            for regressiva in range(5, -1, -1):
                print(regressiva, end=" ", flush = True)
                sleep(1)
            print("\nToken expirado!")

        else:
            print("Opção inválida. Tente novamente...")

    except ValueError:
        print("Opção inválida. Tente novamente...")

print("ENCERRANDO O PROGRAMA...")
sleep(2)
