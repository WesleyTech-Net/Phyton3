supermercado = (
    "Arroz 5kg", 22.90,
    "Feijão 1kg", 7.50,
    "Macarrão 500g", 4.20,
    "Óleo de soja 900ml", 6.80,
    "Leite 1L", 4.99,
    "Café 500g", 12.75,
    "Açúcar 1kg", 3.60,
    "Farinha de trigo 1kg", 5.10,
    "Detergente 500ml", 2.45,
    "Sabão em pó 1kg", 9.90,
    "Papel higiênico 4 rolos", 8.30,
    "Frango congelado 1kg", 11.40,
    "Carne bovina 1kg", 34.90,
    "Refrigerante 2L", 6.25,
    "Biscoito recheado 120g", 2.80
)

print(30 * "-=")
print(f'{"LISTA DE PREÇOS / MERCADO FIGUEIRA":^60}')
print(30 * "-=")

for i in range(0, len(supermercado)):
    if i % 2 == 0:
        print(f"{supermercado[i]:.<30}", end = "R$ ")
    else:
        print(f"{supermercado[i]:>8.2f}")
