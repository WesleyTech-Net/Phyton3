dados = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
    }

media_por_setor = {}

#calcula a media de idade de cada setor
for setor, idade in dados.items():
    media = sum(idade) / len(idade)
    media_por_setor[setor] = media

print("Iadade média de cada setor: ")
#separa de forma organizada a media de idade de cada setor
for setor, media in media_por_setor.items():
    print(f"{setor}: média de {round(media)} anos.")

total_media_geral = sum(media_por_setor.values()) / len(media_por_setor)
print(f"Total da media geral: {round(total_media_geral)} anos")

#contar quantas pessoas estão acima da média geral

cont = 0
for idades in dados.values(): #Percorre cada lista de idades dos setores.
    for idade in idades: # percorre cada idade individual da lista de um setor.
        if idade > total_media_geral:
            cont += 1
print(f"Total de pessoas acima da idade média geral: {cont} pessoa(s).")