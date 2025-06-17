#Escreva um algoritmo que mostra, na tela, quatro produtos a serem comprados em uma lanchonete 
#COXINHA: R$ 5,00
#PASTEL - R$ 7,00
#CAFÉ - R$ 4,00
#SUCO - R$ 6,00
#FAÇA UM ALGORITMO EM QUE VOCÊ SELECIONA O PRODUTO QUE QUER COMPRAR E A QUANTIDADE. FAÇA ISSO ATÉ QUE DECIDA ENCESSAR O PROGRAMA
#AO FINAL, MOSTRE O VALOR FINAL DO PEDIDO A SER PAGO

print("LANCHONETE")
print("1 - COXINHA R$ 5,00")
print("2 - PASTEL R$ 7,00")
print("3 - CAFÉ R$ 4,00")
print("4 - SUCO R$ 6,00")
print("5 - SAIR")

total = 0
while True:
    op = int(input("Qual item gostaria de comprar? "))
    

    if(op == 1):
        qtd = int(input("Quantas unidades quer comprar?"))
        total = total + qtd * 5
    elif(op == 2):
        qtd = int(input("Quantas unidades quer comprar?"))
        total = total + qtd * 7
    elif(op == 3):
        qtd = int(input("Quantas unidades quer comprar?"))
        total = total + qtd * 4
    elif(op == 4):
        qtd = int(input("Quantas unidades quer comprar?"))
        total = total + qtd * 6
    elif(op == 5):
        break
    else:
        print("Produto inválido. Selecione outro...")

print(f"O total a ser gasto nesse pedido é de R$ {total:.2f}")