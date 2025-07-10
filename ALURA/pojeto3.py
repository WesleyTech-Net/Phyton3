quantidade_litro = int(input("Quantos litros de combustível? "))
PRECO_ETANOL = 1.70
PRECO_DIESEL = 2
print("""ESCOLHA DO COMBUSTÍVEL:
      [1] - ETANOL
      [2] - DIESEL
      """)
opcao_combustivel = int(input(">> "))

if opcao_combustivel == 1 and quantidade_litro <= 15:
    desconto15 = PRECO_ETANOL * 2 / 100
    valor_desconto15 = PRECO_ETANOL * quantidade_litro * desconto15
    total15 = PRECO_ETANOL * quantidade_litro - valor_desconto15
    print(f"O desconto é de 2% até 15 litros. Total: R$ {total15:.2f}")
elif opcao_combustivel == 1 and quantidade_litro >= 16:
    desconto15 = PRECO_ETANOL * 4 / 100
    valor_desconto15 = PRECO_ETANOL * quantidade_litro * desconto15
    total15 = PRECO_ETANOL * quantidade_litro - valor_desconto15
    print(f"O desconto é de 4% acima de 15 litros. Total: R$ {total15:.2f}")

elif opcao_combustivel == 2 and quantidade_litro <= 15:
    desconto15 = PRECO_DIESEL * 3 / 100
    valor_desconto15 = PRECO_DIESEL * quantidade_litro * desconto15
    total15 = PRECO_DIESEL * quantidade_litro - valor_desconto15
    print(f"O desconto é de 3% até 15 litros. Total: R$ {total15:.2f}")
elif opcao_combustivel == 2 and quantidade_litro >= 16:
    desconto15 = PRECO_DIESEL * 5 / 100
    valor_desconto15 = PRECO_DIESEL * quantidade_litro * desconto15
    total15 = PRECO_DIESEL * quantidade_litro - valor_desconto15
    print(f"O desconto é de 5% até 15 litros. Total: R$ {total15:.2f}")


