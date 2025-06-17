print("Seja Bem-Vindo a Loja Wesley Sampaio")

#entrada para o cliente inserir valor do pedido e a quantidade de parcelas
valorDoPedido = float(input('Qual o valor do pedido? '))
quantidadeDeParcelas = int(input('Qual a quantidade de parcelas desejadas? '))

#condição para mostrar o valor das parcelas somada aos juros de 0% e o valor total final parcelado
if quantidadeDeParcelas < 4:
    juros = (valorDoPedido * 1) / 100
    valorDaParcela = (valorDoPedido * juros) / quantidadeDeParcelas
    valorTotalParcelado = valorDaParcela * quantidadeDeParcelas
    print(f"O valor das parcelas é de: R$ {valorDaParcela:.2f}.\nO valor total parcelado é de: R$ {valorTotalParcelado}")

#condição para mostrar o valor das parcelas somada aos juros de 4% e o valor total final parcelado
elif quantidadeDeParcelas >= 4 and quantidadeDeParcelas < 6:
    juros = (valorDoPedido * 4) / 100
    valorDaParcela = (valorDoPedido + juros) / quantidadeDeParcelas
    valorTotalParcelado = valorDaParcela * quantidadeDeParcelas
    print(f"O valor das parcelas é de: R$ {valorDaParcela:.2f}.\nO valor total parcelado é de: R$ {valorTotalParcelado}")
    
#condição para mostrar o valor das parcelas somada aos juros de 8% e o valor total final parcelado
elif quantidadeDeParcelas >= 6 and quantidadeDeParcelas < 9:
    juros = (valorDoPedido * 8) / 100
    valorDaParcela = (valorDoPedido + juros) / quantidadeDeParcelas
    valorTotalParcelado = valorDaParcela * quantidadeDeParcelas
    print(f"O valor das parcelas é de: R$ {valorDaParcela:.2f}.\nO valor total parcelado é de: R$ {valorTotalParcelado}")

#condição para mostrar o valor das parcelas somada aos juros de 16% e o valor total final parcelado
elif quantidadeDeParcelas >= 9 and quantidadeDeParcelas < 13:
    juros = (valorDoPedido * 16) / 100
    valorDaParcela = (valorDoPedido + juros) / quantidadeDeParcelas
    valorTotalParcelado = valorDaParcela * quantidadeDeParcelas
    print(f"O valor das parcelas é de: R$ {valorDaParcela:.2f}.\nO valor total parcelado é {valorTotalParcelado}")

#condição para mostrar o valor das parcelas somada aos juros de 32% e o valor total final parcelado
else:
    juros = (valorDoPedido * 32) / 100
    valorDaParcela = (valorDoPedido + juros) / quantidadeDeParcelas
    valorTotalParcelado = valorDaParcela * quantidadeDeParcelas
    print(f"O valor das parcelas é de: R$ {valorDaParcela:.2f}.\nO valor total parcelado é de: R$ {valorTotalParcelado}")