soma = 0 # acumulador
cont = 0 # contador 
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont += 1 #contador mais 1 que achoe
        soma += i #acumulador soma os valores
print(f"A soma de todos os {cont} valores múltiplos de 3, entre 0 e 500 é {soma}")