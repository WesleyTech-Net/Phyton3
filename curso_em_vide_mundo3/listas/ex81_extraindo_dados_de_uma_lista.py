valores = list()

cont = 1
cont2 = 0
while True:
    try:
        
        num = int(input(f"Digite o {cont}º valor: "))
        cont += 1
        cont2 += 1
        valores.append(num)
        op = str(input("Deseja continuar (S/N)? ")).strip().upper()[0]

        if op in "S":
            continue
        elif op in "N":
            print("PROGRAMA TERMINOU")
            break
        
    except ValueError:
        print("❌ Valor inválido tente novamente...")

print("Você inseriou os valores: ", end="")

for i in valores:
    print(i, end = " ")
    
print(f"\nVocê digitou {cont2} número(s)")

decrescente = valores.copy()
decrescente.sort(reverse=True)
print(f"Lista ordenada de forma decrescente: {decrescente}")
    