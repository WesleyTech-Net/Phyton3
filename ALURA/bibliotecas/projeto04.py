from math import sqrt

listaDeNumeros= [2, 8, 15, 23, 91, 112, 256]
inteiros = []

for i in listaDeNumeros:
    raizQuadrada = sqrt(i)
    if raizQuadrada // 1 == raizQuadrada:
        inteiros.append((i, int(raizQuadrada)))

for numero, raiz in inteiros:
    print(f"{numero} ➡️  raiz = {raiz}")