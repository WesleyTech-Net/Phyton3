#Dado uma lista contendo as notas de alunos em uma disciplina, escreva uma expressão para:
# notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
# a) Encontrar quantos alunos tiraram nota 7
# b) Alterar a última nota para 4
# c) Encontrar a maior nota
# d) Ordenar a lista de notas
# e) A média das notas

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

#letra a)
print(notas.count(7))

#letra b)
notas[-1] = 4
print(notas)

#letra c)
print(max(notas))

#letra d)
notas.sort()
print(notas)

#letra e)
print(sum(notas) / len(notas))