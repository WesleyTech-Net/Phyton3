print(10 * "-=")
print("PROGRESSÃO ARITMÉTICA")
print(10 * "-=")

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1
while cont <= 10:
    print(f"{termo} > ", end="")
    termo += razao
    cont += 1
print("FIM DA PROGRESSÃO")