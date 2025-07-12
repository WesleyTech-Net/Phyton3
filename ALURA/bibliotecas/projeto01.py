from random import choice
lista_usuarios = []
sorteados = []
cont = 1

print(10 * "-=","SORTEIO FACEBOOK",10 * "-=")

numero_p = int(input("Insira o número de participantes: "))
for i in range(1, numero_p + 1):
    lista_usuarios.append(cont)#para colocar os itens dentro da lista_usuarios
    cont += 1

while True:

    try:
        
        sorteio = choice(lista_usuarios)#para escolher de forma aleatória os itens da lista_usuarios
        print(f"O número sorteado foi {sorteio}")
        sorteados.append(sorteio)#para adicionar os valores sorteados a lista sorteados
        lista_usuarios.remove(sorteio)#para não repetir os números da lista

        escolha = str(input("Deseja continuar o sorteio (S/N): ")).strip().upper()[0]

        if escolha == 'N':
            break
        if not lista_usuarios:
            break

    except ValueError:
        print("🚫 Valor numérico inválido. Tente novamente...")

print(f'{"RESULTADO DO SORTEIO":=^35}')
print(f"\nOs números sorteados foram: ", end = "")
for i in sorteados:
    print(f"{i}", end = " ")
