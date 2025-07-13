id_par = []
id_impar = []

cont = 1
for i in range(1, 11):

    try:
        id = int(input(f"Insira o {i}º ID Par para doces ou ID ímpar para amargos: "))
        cont += 1
        if id % 2 == 0:
            if id not in id_par:
                id_par.append(id)
            else:
                print("ID para doce já inserido. Tente novamente...")
        else:
            if id not in id_impar:
                id_impar.append(id)
            else:
                print("ID para amargos já inserido. Tente novamente...")
            
    except ValueError:
        print("Valor numérico inválido. Tente novamente...")


print(f"{'LISTA DE IDs':-^40}")
print(f"Os IDs para doces são: ", end="")
for i in id_par:
    print(i, end = " ")

print(f"\nOs IDs para amargos são: ", end="")
for i in id_impar:
    print(i, end = " ")
