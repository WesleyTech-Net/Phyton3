from random import choice

#lista dos itens
frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

salada_frutas_surpresa = [choice(frutas) for surpresa in range(3)]#escolhe três itens aleatórios da lista FRUTAS

print("Salada de frutas surpresa: ")
for i, fruta in enumerate(salada_frutas_surpresa, 1):
    print(f"{i}º item surpresa: {fruta}")
