maiorPeso = 0
menorPeso = 0
for i in range (1, 6):
    pesoPessoas = float(input(f"Peso da {i}º pessoa: "))
    if i == 1:
        maiorPeso = pesoPessoas
        menorPeso = pesoPessoas
    else:
        if pesoPessoas > maiorPeso:
            maiorPeso = pesoPessoas
        if pesoPessoas < menorPeso:
            menorPeso = pesoPessoas
print(f"O maior peso foi de {maiorPeso} kg.")
print(f"O menor peso foi de {menorPeso} kg.") 