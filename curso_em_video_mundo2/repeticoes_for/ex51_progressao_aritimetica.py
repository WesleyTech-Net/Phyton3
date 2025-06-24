print(20 * "=")
print("10 TERMOS DE UMA PA")
print(20 * "=")
soma = 0
razao = int(input("Qual a razao: "))
termo = int(input("Qual o termo: "))
decimo = termo + (10 - 1) * razao
for i in range(termo, decimo, razao):
    print(f"{i}", end = " -> ")
print("ACABOU")