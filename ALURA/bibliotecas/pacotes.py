#utilizando BAR
import matplotlib.pyplot as plt

estudante = ["João", "Maria", "Pedro"]
notas = [8, 9, 6.5]

plt.bar(x = estudante, height = notas)
plt.show()

#importando uma função específica de uma biblioteca
estudante_2 = ["João", "Maria", "Pedro", "José", "Vitor"]

from random import choice

estudante_escolha = choice(estudante_2)

print(estudante_escolha)


