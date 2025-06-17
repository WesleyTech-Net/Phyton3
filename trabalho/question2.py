#boas-vindas ao cliente 
print(8 * '-',"Bem-vindo a Loja de Marmitas de Wesley Sampaio", 7 * '-')
print(26 * '-', "CARDÁPIO", 27 * '-')

#mostrar o cardápio ao cliente
print(3 * '-', "| Tamanho | Bife Acebolado (BA) | Filé de Frango (FF) |", 3 * '-')
print(3 * '-', "|    p    |       R$ 16.00      |         R$ 15.00    |", 3 * '-')
print(3 * '-', "|    M    |       R$ 18.00      |         R$ 17.00    |", 3 * '-')
print(3 * '-', "|    G    |       R$ 22.00      |         R$ 21.00    |", 3 * '-')
print(63 * "-")

total = 0

while True:

    #pedir para o cliente o sabor
    sabor = input("Entre com o sabor desejado BA/FF: ")
    
    total += 0

    #condição se o cliente errar o sabor BA e o tamanho
    if sabor == "BA":
    
    #cliente escolhe o tamanho para o sabor Bife Acebolado (BA) 
        tamanho = input("Entre com o tamnho desejado (P/M/G): ")
        if tamanho != "P" and tamanho != "M" and tamanho != "G":
            print("Tamanho inválido. Tente novamente...\n")
            continue
        else:
            if tamanho == "P":
                valor = 16
                print(f"Você pediu um Bife Acebolado no tamanho {tamanho}: R$ {valor:.2f}")
                total += valor
            elif tamanho == "M":
                valor = 18
                print(f"Você pediu um Bife Acebolado no tamanho {tamanho}: R$ {valor:.2f}")
                total += valor
            elif tamanho == "G":
                valor = 22
                print(f"Você pediu um Bife Acebolado no tamanho {tamanho}: R$ {valor:.2f}")
                total += valor
    
    if sabor == "FF":
    #cliente escolhe o tamanho para o sabor Filé de Frango (FF)
        tamanho = input("Entre com o tamnho desejado (P/M/G): ")
        if tamanho != "P" and tamanho != "M" and tamanho != "G":
            print("Tamanho inválido. Tente novamente...\n")
            continue
        else:
            if tamanho == "P":
                valor = 15
                print(f"Você pediu um Filé de Frango no tamanho {tamanho}: R$ {valor:.2f}")
                total += valor
            elif tamanho == "M":
                valor = 17
                print(f"Você pediu um Filé de Frango no tamanho {tamanho}: R$ {valor:.2f}")
                total += valor
            elif tamanho == "G":
                valor = 21
                print(f"Você pediu um Fiçé de Frango no tamanho {tamanho}: R$ {valor:.2f}")
                total += valor

    #condição caso o cliente erre a entrada do sabor
    if sabor != "BA" and sabor != "FF":
        print("Sabor inválido. Tente novamente...\n")
        continue

    #condição caso o cliente escolha continuar e fazer outros ou pediso ou terminar os pedios 
    escolha = input("\nDeseja mais alguma coisa (S/N): ")
    if escolha == "S":
        continue
    else:
        print(f"\nO valor total a ser pago: R${total}")       
        break