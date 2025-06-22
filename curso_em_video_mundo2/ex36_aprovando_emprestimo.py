valorCasa = float(input("Insira o valor da casa? "))
salario = float(input("Qual o seu salário? R$ "))
parcelas = int(input("Quantos anos deseja pagar? "))

meses = parcelas * 12
parcelaTotal = valorCasa / meses
prestacaoMensal = (salario * 30) / 100


if prestacaoMensal > parcelaTotal:
    print(f"Com base no seu salário de R$ {salario} e o valor da casa de R$ {valorCasa}")
    print(f"Par pagar esse valor em {parcelas} anos, o valor ficou no total de R$ {parcelaTotal:.2F}. EMPRÉSTIMO APROVADO!")
else:
    print(f"Com base no seu salário de R$ {salario} e o valor da casa de R$ {valorCasa}")
    print(f"Par pagar esse valor em {parcelas} anos, o valor ficou no total de R$ {parcelaTotal:.2F}. EMPRÉSTIMO NEGADO!")
