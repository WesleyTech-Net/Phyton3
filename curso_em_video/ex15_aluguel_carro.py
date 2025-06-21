dias = int(input("Insira os dias: "))
distancia = float(input("Insira os km rodados: "))
diaria = dias * 60
kmRodado = distancia * 0.15
valorTotal = diaria + kmRodado
print(f"O total a pagar é de R${valorTotal:.2f}")