n = int(input("Insira um número: "))
print(f"Calculcando {n}! = ", end="")

cont = n
fat = 1
while cont > 0:
    print(f"{cont}", end="")
    print(" x " if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print(f"{fat}")


