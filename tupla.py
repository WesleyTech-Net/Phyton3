mochila = ("Machado", "Camisa", "Caderno", "Lápis")
print(mochila)
print(mochila[0])
print(mochila[1])
print(mochila[0:2])
print(mochila[2:])
print(mochila[-1])

#varredura
for item in mochila:
    print(f"Na mochila tem: {item}")

#forma tradicional
tam = len(mochila)
for i in range(0, tam, 1):
    print(f"Na minha mochila tem: {mochila[i]}")