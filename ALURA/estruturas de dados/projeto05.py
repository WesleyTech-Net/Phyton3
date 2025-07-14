vendas = {
    'Produto A': 300, 
    'Produto B': 80, 
    'Produto C': 60,
    'Produto D': 200, 
    'Produto E': 250, 
    'Produto F': 30
    }

total = sum(vendas.values())#vai somar todas as vendas
print(f"O total de vendas: R$ {total}")

mais_vendido = max(vendas, key=vendas.get)#vai separar o produto mais vendido 
print(f"O produto mais vendido foi o {mais_vendido} como valor de R${vendas[mais_vendido]}")