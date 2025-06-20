mercado = []
for i in range(3):
    nome = input("Nome do item: ")
    qtd = int(input('Quantidade do item: '))
    valor = float(input('Preço do item: '))
    mercado.append([nome, qtd, valor])
print(mercado)

soma = 0
print('Lista de Compras')
print(20 * "-")
print('item | Quantidade | Valor unitário | Total do item |')
for item in mercado:
    print(f"{item[0]} | {item[1]} | {item[2]} | {item[1] * item[2]}")
    soma += item[1] * item[2]
print(20 * "-")
print(f"Total a ser pago: {soma}")
    