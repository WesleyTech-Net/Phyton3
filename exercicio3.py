frase = input('Digite uma frase: ')
tamanho = len(frase)

frase2 = frase[:int(tamanho/3)]
print(frase2[-3:])