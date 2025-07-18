num = int(input("Insira um número inteiro"))

def tabuada(numero: int):   
    print(f'Tabuada do {numero}:')
    for i in range(11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

tabuada(num)