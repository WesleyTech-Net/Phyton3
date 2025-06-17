def realce(s1):
    print("|", 20 * "_", "|")
    print("|", 20 * "_", "|")
    print(s1)
    print("|", 20 * "_", "|")
    print("|", 20 * "_", "|")

realce("BEM VINDO AO PROGRAMA")

#exemplo 2

def cont(x, y):
    res = x + y
    print("\n", res)

cont(4, 9)

#exemplo sem parâmetros opcionais

def soma(x, y, z):
    resp = x + y + z
    print(resp)
soma(4, 5, 6)

#exemplo com parâmetros opcionais 

def soma2(x = 0, y = 0, z = 0):
    resp = x + y + z
    print(resp)

soma2(4, 4, 4)
soma2(4, 4)
soma2(4)
soma2()