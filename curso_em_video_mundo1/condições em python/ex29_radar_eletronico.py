v = float(input("Qual a velocidade atual do carro? "))

if v > 80:
    multa = (v - 80) * 7
    print(f"Você excedeu o limite de velocidade de 80 km/h.\nO valor total da multa é: R$ {multa:.2f}")
else:
    print("Tenha um ótimo dia! Dirija com segurança!")