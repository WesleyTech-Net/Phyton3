import matplotlib.pyplot as plt

bacterias_dia = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
percentual_crescimento = []


for i in range(1, len(bacterias_dia)):
    amostra_passada = bacterias_dia [i - 1]
    amostra_atual = bacterias_dia[i]
    crescimento_percentual = 100 * (amostra_atual - amostra_passada) / amostra_passada
    percentual_crescimento.append(round(crescimento_percentual, 2))

print("Percentual de crescimento por dia: ", end = "")
for c in percentual_crescimento:    
    print(f"{c}%", end=", ")

