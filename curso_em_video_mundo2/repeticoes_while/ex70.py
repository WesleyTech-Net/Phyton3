titulo = "LOJA APAE"
titulo_final = "TOTAL DA COMPRA"
print(10 * '-=')
print(titulo.center(20, " "))
print(10 * '-=')

cont = 0
valor_total = 0
menor = 0
total_1000 = 0
barato = ''

while True:

    produto = str(input("Nome do produto: ")).strip().upper()
    preco = float(input("Preço do produto: "))
    op = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
    cont += 1
    valor_total += preco
    

    if op in "S":
        if preco >= 1000:
            total_1000 += 1

        if cont == 1:
            menor = preco
            barato = produto
        else:
            if preco < menor:
                menor = preco
                barato = produto
        continue
    
    elif op in "N":
        break

print(10 * '-=')
print(titulo_final.center(20, " "))
print((f"Valor total da compra: R$ {valor_total}"))
print(f"Temos {total_1000} produtos custando mais de R$ 1.000,00")
print(f"O produto mais barato foi {barato} que custa R$ {menor}")