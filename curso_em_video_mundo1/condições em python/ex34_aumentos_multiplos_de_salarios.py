salario = float(input("Qual é o salário do funcionário? R$ "))

if salario <= 1250:
    aumento = (salario * 15) / 100
    aumentoTotal = aumento + salario
    print(f"Quem ganhava {salario} passará a ganhar {aumentoTotal:.2f}")
else:
    aumento = (salario * 10) / 100
    aumentoTotal = aumento + salario
    print(f"Quem ganhava {salario} passará a ganhar {aumentoTotal:.2f}")  