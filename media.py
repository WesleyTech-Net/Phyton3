nome = str(input('Nome Completo do Aluno: '))
disciplina = str(input('Disciplina: '))
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a teceira nota: '))
n4 = int(input('Digite a quarta nota: '))
m = (n1 + n2 + n3 + n4) / 4
print(f'O aluno {nome} obteve uma média de {m} pontos, na disciplina de {disciplina}')