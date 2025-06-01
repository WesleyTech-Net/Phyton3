aluno = str(input('Nome do aluno: '))
disciplina = str(input('Disciplina: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
m = (n1 + n2 + n3 + n4) / 4
print(f'O aluno {aluno} obteve uma média {m} pontos, na disciplina de {disciplina}')
