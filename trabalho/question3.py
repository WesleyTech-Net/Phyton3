print("Bem vindo Fábrica de Camisetas de Wesley Sampaio\n")

def escolha_modelo():
    while True:

        print("Entre com o modelo desejado")
        print("MCS - MANGA CURTA SIMPLES \nMLS - MANGA LONGA SIMPLES \nMCE - MANGA CURTA COM ESTAMPA \nMLE = MANGA LONGA COM ESTAMPA")
        global valor
        escolha_modelo = input(">>")
        if escolha_modelo != "MCS" and escolha_modelo != "MLS" and escolha_modelo != "MCE" and escolha_modelo != "MLE":
            print("Escolha inválida, entre com o modelo novamante...\n")
            continue
        if escolha_modelo == "MCS":
            valor = 1.80
        if escolha_modelo == "MLS":
            valor = 2.10
        if escolha_modelo == "MCE":
            valor = 2.90
        if escolha_modelo == "MLE":
            valor = 3.20

        return escolha_modelo
escolha_modelo()

def num_camisetas():
    while True:

        try:
            global total
            qtde = int(input("Entre com o número de camisetas: "))
            if qtde > 20000:
                print("Não aceitamos tantas camisetas de uma vez.")
                continue
            if qtde < 20:
                total = qtde * valor
                desconto = total * 100 / 100
                total_desc = total - desconto
                print(f"O valor total somado ao desconto é de: R${total_desc}")
            if qtde >= 20 and qtde < 200:
                total = qtde * valor
                desconto = total * 5 / 100
                total_desc = total -desconto
                print(f"O valor total é de R$ {total_desc}")
            break
        except ValueError:
            print("Por favor, entre com o número de camisetas novamente.")
            continue
        

    return qtde
num_camisetas()