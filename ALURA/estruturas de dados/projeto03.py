print(f"{'GABARITO DA PROVA':-^50}")

gabarito = {
    1:"D",
    2:"A",
    3:"C",
    4:"B",
    5:"A",
    6:"D",
    7:"C",
    8:"C",
    9:"A",
    10:"B"
}

acertos = 0
for i in range(1, 11):
        
    while True:
        resposta = str(input(f"{i}º - ")).strip().upper()
        if resposta and resposta[0] in ["A", "B", "C", "D"]:
            resposta == resposta[0]
            if resposta == gabarito[i]:
                acertos += 1
            break
        else:
            print("Opção Inválida. Digite apenas A, B, C ou D")
    
print(f"Você acertou {acertos} de 10 questões.")