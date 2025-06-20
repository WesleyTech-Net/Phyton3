def soma(*num):
    acumulador = 0
    print(f"Tupla: {num}")
    for i in num:
        acumulador += i
    return acumulador

#programa principal
print(f'Resultado: {soma(1, 2)}')
print(f'Resultado: {soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 20, 50, 70)}')