distancia = float(input("Qual a distância da viagem? "))

if distancia <= 200:
    total = distancia * 0.5
    print(f"A distância total da sua viagem é de {distancia} km.\nO valor total é de: R$ {total:.2f}")
else:
    total = distancia * 0.45
    print(f"A distância toal da sua viagem é de {distancia} km.\nO valor total é de: R$ {total:.2f}")