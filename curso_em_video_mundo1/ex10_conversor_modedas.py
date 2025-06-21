real = float(input("Insira o valor (R$): "))
dolar = real / 5.51
euro = real / 6.35
print(f"O valor de R${real} equivale a ${dolar:.2f} e £{euro:.2f}")