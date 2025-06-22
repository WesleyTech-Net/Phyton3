print(10 * '=', "LOJAS WESLEY", 10 * '=' )
preco = float(input("Valor total da Compra: R$ "))
print(""" Formas de pagamento
      [1] - À vista dinheiro 
      [2] - À vista no cartão / débito
      [3] - Até 8x sem juros.
      [4] - Parcela acima de 8x.""")

try:
    opcao = int(input("Qual opção? "))
    if opcao == 1:
        desconto = (preco * 12) / 100
        descontoTotal = preco - desconto
        print(f"Sua compra de R$ {preco} ficará no valor de R$ {descontoTotal}.")
    elif opcao == 2:
        desconto = (preco * 7) / 100
        descontoTotal = preco - desconto
        print(f"Sua compra de R$ {preco} ficará no valor de R$ {descontoTotal}.")
    elif opcao == 3:
        parcela = int(input("Quantidade de parcelas desejadas: "))
        parcelaTotal = preco / parcela
        desconto = (preco * 100) / 100
        descontoTotal = desconto
        print(f"O valor das parcelas ficará no valor de R$ {parcelaTotal:.2f}. O total final será de:R$ {descontoTotal}.")
    elif opcao == 4:
        parcela = int(input("Quantidade de parcelas desejadas: "))
        desconto = (preco * 20) / 100
        descontoTotal = preco + desconto
        parcelaTotal = descontoTotal / parcela        
        print(f"O valor das parcelas ficará no valor de R$ {parcelaTotal:.2f}. O total final será de:R$ {descontoTotal}.")
    else:
        print("Opção inválida. Tente novamente...")
except ValueError:
    print("Opção inválida. Tente novamente...")
