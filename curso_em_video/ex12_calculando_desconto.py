produto = float(input("Insira o valor do produto: "))
desconto = (produto * 10) / 100
totalDesconto = produto - desconto
print(f"Esse produto de R${produto} sairá no valor Total de R${totalDesconto:.2f} com 10% de desconto.")