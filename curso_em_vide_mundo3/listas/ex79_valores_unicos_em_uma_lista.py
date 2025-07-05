valores = list()

cont = 1
while True:

    try:
        
        num = (int(input(f"Digite o {cont}º valor: ")))
        
        
        
        if num in valores:
            print("Valor já inserido tente novamente...")

        else:

            cont += 1
            valores.append(num)
            print("✅ Valor adicionado com sucesso...")
            op = str(input("Quer continuar: [S/N] ")).strip().upper()[0]
            
            if op in "S":
                continue
            elif op in "N":
                break
        
    except ValueError:
        print("Valor inválido tente novamente...")
        continue

print("Você adicionou os valores: ", end="")
for i in valores:
    print(f"{i}", end=" ")