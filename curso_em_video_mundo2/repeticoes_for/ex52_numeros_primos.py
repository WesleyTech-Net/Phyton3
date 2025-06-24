num = int(input("Insira um número: "))
cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        print("\33[34m", end = "")
        cont += 1
    else:
        print("\33[31m", end = "")
    print(f"{i}", end=" ")
print(f"\n\033[mO número {num} foi divisível {cont} vezes")
if cont == 2:
    print("Sendo asism, é um número PRIMO!")
else:
    print("Por isso não é um número PRIMO!")