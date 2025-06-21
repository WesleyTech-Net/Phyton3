import random

a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")

listaDeAlunos = [a1, a2, a3, a4]
sorteio = random.shuffle(listaDeAlunos)
print(f"A ordem da apresentação será:")
print(listaDeAlunos)