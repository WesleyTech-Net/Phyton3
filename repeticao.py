x = 1
while (x <= 200):
    print(x)
    x = x + 1 #incrementador 

#exemplo
incial = int(input('Valor inicial: '))
final = int(input('Valor final: '))

x = incial
while (x <= final):
    if (x % 2 == 0):
        print(x)
    x = x + 1