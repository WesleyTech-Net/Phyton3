print('Digite uma mensagem que irei repetir pra você!')
print('Para encerrar escreva "sair"')
while True:
    texto = input('')
    print(texto)
    if texto == 'SAIR' or texto == 'sair':
        break

print('Encerrando o programa...')