from random import randint 
numeros = randint(1,10), randint(1, 10), randint(1, 10), randint(1, 10)

print(f"Os números sorteados são: ", end="")

for i in numeros:
    print(f"{i}", end=", ")
print(f"\nO maior valor sorteado foi {max(numeros)}")
print(f"O menor valor sorteado foi {min(numeros)}")
