print(10 * "-=")
print("PROGRESSÃO ARITMÉTICA")
print(10 * "-=")

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo} > ", end="")
        termo += razao
        cont += 1
    print("FIM DA PROGRESSÃO")
    mais = int(input("Quantos termos a mais você quer? "))
print("OBRIGADO!")