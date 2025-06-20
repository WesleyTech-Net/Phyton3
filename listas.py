#podemos alterar os dados

food = ["Laranja", "Lasanha", "Bacon", "Macarrão"]

print(f"Lista: {food}")

food[0] = "Arroz"

print(f"Lista: {food}")

#adiciona ao final da lista
food.append("Churrasco")
print(f"Lista: {food}")

#insere na posição informada
food.insert(2, "Strogonoff")
print(f"Lista: {food}")

#deleta do índice informado
del food[2]
print(f"Lista: {food}")

#deleta o dado informado
food.remove("Macarrão")
print(f"Lista: {food}")

#cópia de listas
lista_original = [5, 6, 7, 8, 9]
lista_referenciada = lista_original[:]
print(lista_original)
print(lista_referenciada)

lista_referenciada[0] = 2
print(lista_original)
print(lista_referenciada)