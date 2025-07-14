dados = {
    'Área Norte': [2819, 7236],
    'Área Leste': [1440, 9492],
    'Área Sul': [5969, 7496],
    'Área Oeste': [14446, 49688],
    'Área Centro': [22558, 45148]
}

media_por_area = {}
maior_diversidade = 0
for area, especie in dados.items():
    media = sum(especie) / len(especie)
    media_por_area[area] = media

    total_especies = sum(especie)
    if total_especies > maior_diversidade:
        maior_diversidade = total_especies
        area_mais_diversa = area

print("Média de espécies por área: ")
for area, media in media_por_area.items():
    print(f"{area}: {media:.2f} espécies")

print(F"A área com a mairo diversidade biológica: {area_mais_diversa} ({maior_diversidade} espécies)")

