salario = float(input("Qual o sálrio do Funcionário: "))
aumento = (salario * 15) / 100
reajuste = salario + aumento
print(f"O funcionário 1 ganha R${salario} passará a ganhar R${reajuste:.2f} com 15% de aumento.")