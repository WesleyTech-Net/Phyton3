num = list()

for i in range(1, 5):
    num.append(int(input(f"Digite o {i} º valor: ")))

print("\nVocê digitou os valores: ", end="")
for i in num:
    print(i, end=" ")

print(f"\nO maior valor digitado foi {max(num)} na posição {num.index(max(num))}")
print(f"O menor valor digitado foi {min(num)} na posição {num.index(min(num))}")

