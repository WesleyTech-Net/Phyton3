info = {'Nome Completo': [], 'Idade': [], 'Profissão': []}
for i in range(1):
    nome = input('Insira seu nome Completo: ')
    idade = int(input('Insira sua idade: '))
    prof = input('Insira sua profissão: ')
    info['Nome Completo'].append(nome)
    info['Idade'].append(idade)
    info['Profissão'].append(prof)
print(20 * "-")
print(info)