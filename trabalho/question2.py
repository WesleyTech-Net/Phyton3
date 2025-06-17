#boas-vindas ao cliente 
print(5 * '-',"Bem-vindo a Loja de Marmitas de Wesley Sampaio", 5 * '-')
print(23 * '-', "CARDÁPIO", 25 * '-')

#mostrar o cardápio ao cliente
print(3 * '-', "| Tamanho | Bife Acebolado (BA) | Filé de Frango (FF) |", 3 * '-')
print(3 * '-', "|    p    |       R$ 16.00      |         R$ 15.00    |", 3 * '-')
print(3 * '-', "|    M    |       R$ 18.00      |         R$ 17.00    |", 3 * '-')
print(3 * '-', "|    G    |       R$ 22.00      |         R$ 21.00    |", 3 * '-')

total = 0
while True:

    sabor = input("Entre com o sabor desejado BA/FF: ")
    
    if (sabor == 'BA'):
        tamanho = input("Entre com o tamanho desejado P/M/G: ")
        if (tamanho == "P"):
            valor = 16
            total = total + valor
            print(f"Você pediu um Bife Acebolado no tamanho {tamanho}: R$ {valor:.2f}")
        if (tamanho == "M"):
            valor = 18
            total = total + valor
            print(f"Você pediu um Bife Acebolado no tamanho {tamanho}: R$ {valor:.2f}")
        if (tamanho == "G"):
            valor = 22
            total = total + valor
            print(f"Você pediu um Bife Acebolado no tamanho {tamanho}: R$ {valor:.2f}")                 
            
        escolha = input("\nDeseja mais alguma coisa? (S/N): ")
        if (escolha == "S"):
            continue
        else:
            total = total + valor
            print(f"O valor total a ser pago: R${total}")
            break 
    
    elif (sabor == 'FF'):
        tamanho = input("Entre com o tamanho desejado P/M/G: ")
        if (tamanho == "P"):
            valor = 15
            total = total + valor
            print(f"Você pediu um Bife Acebolado no tamanho {tamanho}: R$ {valor:.2f}")
        if (tamanho == "M"):
            valor = 17
            total = total + valor
            print(f"Você pediu um Bife Acebolado no tamanho {tamanho}: R$ {valor:.2f}")
        if (tamanho == "G"):
            valor = 21
            total = total + valor
            print(f"Você pediu um Bife Acebolado no tamanho {tamanho}: R$ {valor:.2f}")                 
            
        escolha = input("\nDeseja mais alguma coisa? (S/N): ")
        if (escolha == "S"):
            continue
        else:
            total = valor
            print(f"O valor total a ser pago: R${total}")
            break 

    else:
        print("Sabor inválido. Tente novamente...")
        continue
    


    