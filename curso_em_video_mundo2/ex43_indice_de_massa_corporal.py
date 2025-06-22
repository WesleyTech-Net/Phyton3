altura = float(input("Insira sua altura: "))
peso = float(input("Insira seu peso: "))

imc = peso / (altura ** 2)
print(f"O seu Índice de Massa Corporal (IMC) é de {imc:.2f}")

if imc <= 18.5:
    print("Você está abaixo do peso")
elif imc <= 25:
    print("Você está no peso ideal.")
elif imc <= 30:
    print("Você está com sobrepeso.")
elif imc <= 40:
    print("Você está com obesidade.")
else:
    print("Você está com OBESIDADE MÓRBIDA.\nProcura ajuda médica urgente!")