quilometragem = float(input('Insira o total de KM: '))
dias = int(input('Insira a quantidade de dias: '))
valorkm = quilometragem * 0.15
diaria = dias * 60
print(f'O valor total do percurso de {quilometragem}Km é igual a R$ {valorkm}')
print(f'O custo por dia é de R$ 60, ficando no valor total de diarias de R$ {diaria}')
print(f'O valor total da locação é de R$ {diaria + valorkm}')