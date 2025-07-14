print(20 * "-=")
print(f"{'TEMPERATURA MÉDIA':-^40}")
print(20 * "-=")

meses = {
    1:"JANEIRO",
    2:"FEVEREIRO",
    3:"MARÇO",
    4:"ABRIL",
    5:"MAIO",
    6:"JUNHO",
    7:"JULHO",
    8:"AGOSTO",
    9:"SETEMBRO",
    10:"OUTUBRO",
    11:"NOVEMBRO",
    12:"DEZEMBRO"
}

lista_temperaturas = list()

#laço para coletar as temperaturas de cada mês e organizar na lista_temperaturas
for i in range(1, 13):
    coleta_temperatura = int(input(f"Temperatura do {i}º mês em °C: "))
    lista_temperaturas.append(coleta_temperatura)

#calculo de média anual das temperaturas coletas
media = sum(lista_temperaturas) / 12

print(40 * ".")
print(f"A temperatura média anual é de {round(media, 1)}°C")

print(f"{'MESES ACIMDA DA MÉDIA ANUAL':-^40}")
for i in range(12):
    if lista_temperaturas[i] > media:
        print(f"{meses[i + 1]}: {round(lista_temperaturas[i], 1)}°C")

