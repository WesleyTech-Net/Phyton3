print(10 * "-")
print("FIBONACCI")
print(10 * "-")


n = int(input("Quantos termos mostrar: "))

termo_1 = 0
termo_2 = 1

print(f"{termo_1} -> {termo_2}", end="")

cont = 3
while cont <= n :
    termo_3 = termo_1 + termo_2
    print(f" -> {termo_3}", end="")
    termo_1 = termo_2
    termo_2 = termo_3
    cont += 1
print("\nFIM")