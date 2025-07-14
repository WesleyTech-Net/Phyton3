print(20 * "-=")
print(f"{'TABELA DE VOTOS DA MARCA':-^40}")
print(20 * "-=")

votos = {
    "Design 1": 1334,
    "Design 2": 982,
    "Design 3": 1751,
    "Design 4": 210,
    "Design 5": 1811,
}

total = sum(votos.values())#soma o total de votos
vencedor = max(votos, key=votos.get)#pega o design com a maior quantidade de votos
print(f"O vencedor foi o {vencedor} com {votos[vencedor]} votos.")


for design, qtde in votos.items():#laço para saber o percentual de votos de cada design
    percentual = (qtde / total) * 100
    print(f"{design}: {qtde} votos {round(percentual, 2)}%")

print(f"Total de votos {total}")

