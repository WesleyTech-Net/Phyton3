def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam < min) or (tam > max)):
        s1 = input(pergunta)
        tam = len(s1)
    return s1
x = valida_string('Digite uma string: ', 5, 30)
print(f"Você digitou a string: {x}. \n Dado válido. Encerrando o progroma...")