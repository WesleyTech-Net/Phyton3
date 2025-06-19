print("Bem vindo Fábrica de Camisetas de Wesley Sampaio\n")

#essa função pede a escolha do modelo de camiseta, incluso com o valor de cada modelo.
def escolha_modelo():
    while True:

        print("Entre com o modelo desejado")
        print("MCS - MANGA CURTA SIMPLES \nMLS - MANGA LONGA SIMPLES \nMCE - MANGA CURTA COM ESTAMPA \nMLE = MANGA LONGA COM ESTAMPA")

        global valor_camiseta

        escolha_modelo = input(">>")
        if escolha_modelo != "MCS" and escolha_modelo != "MLS" and escolha_modelo != "MCE" and escolha_modelo != "MLE":
            print("Escolha inválida, entre com o modelo novamante...\n")
            continue
        if escolha_modelo == "MCS":
            valor_camiseta = 1.80
        if escolha_modelo == "MLS":
            valor_camiseta = 2.10
        if escolha_modelo == "MCE":
            valor_camiseta = 2.90
        if escolha_modelo == "MLE":
            valor_camiseta = 3.20

        return escolha_modelo
    
escolha_modelo()

#essa função pede a escolha de quantidade de camisetas, incluso o desconto para determinada quantidade de camisetas.
def num_camisetas():
    while True:

        try:

            global total_desc

            qtde = int(input("\nEntre com o número de camisetas: "))
            if qtde > 20000:
                print("Não aceitamos tantas camisetas de uma vez.")
                continue
            if qtde < 20:
                total = qtde
                desconto = total 
                total_desc = total
                
            if qtde >= 20 and qtde < 200:
                total = qtde
                desconto = total * 5 / 100
                total_desc = total - desconto
                
            if qtde >= 200 and qtde < 2000:
                total = qtde
                desconto = total * 7 / 100
                total_desc = total - desconto
                
            if qtde >= 2000 and qtde <= 20000:
                total = qtde 
                desconto = total * 12 / 100
                total_desc = total - desconto
                
            break
        except ValueError:
            print("Por favor, entre com o número de camisetas novamente.")
            continue
    return qtde

num_camisetas()

#essa função pede a escolha do frete adicional.
def frete():
    while True:

        global escolha_frete
        try:
            print("Escolha o tipo de frete:")
            print("1 - Frete por transportadora - R$ 100.00 \n2 - Frete por Sedex - R$200.00 \n0 - Retirar pedido na fábrica - R$ 0.00")
            escolha_frete = int(input(">>"))
            if escolha_frete == 0:
                break

            elif escolha_frete == 1:
                break

            elif escolha_frete == 2:
                break
            else:
                continue
        except ValueError:
            continue
    return escolha_frete

frete()

#Aqui temos as condições para a escolha do frete. Mostrando ao final de cada condição, o total do serviço contratado.
if escolha_frete == 0:
    valor_frete = 0
    total = total_desc + valor_frete
    print(f"Total: R$ {total} (Modelo: {valor_camiseta} * Quantidade(com desconto): {total_desc} + frete: {valor_frete})")
    
if escolha_frete == 1:
    valor_frete = 100
    total = total_desc + valor_frete
    print(f"Total: R$ {total} (Modelo: {valor_camiseta} * Quantidade(com desconto): {total_desc} + frete: {valor_frete})")

if escolha_frete == 2:
    valor_frete = 200
    total = (valor_camiseta * total_desc) + valor_frete
    print(f"Total: R$ {total:.2f} (Modelo: {valor_camiseta} * Quantidade(com desconto): {total_desc} + frete: {valor_frete})")

