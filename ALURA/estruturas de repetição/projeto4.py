candito_1 = 0
candito_2 = 0
candito_3 = 0
candito_4 = 0
nulo = 0
branco = 0

print("""
[1] - CANDITO 1
[2] - CANDITO 2
[3] - CANDITO 3
[4] - CANDITO 4
[5] - VOTO NULO
[6] - VOTO EM BRANCO""")

print(25 * "-", "ELEIÇÃO PARA GERÊNCIA", 25 * "-")

for i in range(1, 21):
    
    try:
        voto = int(input(f"{i}º voto: "))

        if voto == 1:
            candito_1 += 1
        elif voto == 2:
            candito_2 += 1    
        elif voto == 3:
            candito_3 += 1
        elif voto == 4:
            candito_4 += 1    
        elif voto == 5:
            nulo += 1
        elif voto == 6:
            branco += 1
        else:
            print("🚫 Voto inválido. Tente novamente...")  
    except ValueError:
        print("🔴 Valor numérico incorreto. Tente novamente...")

total = candito_1 + candito_2 + candito_3 + candito_4
print(f'{"APURAÇÃO DOS VOTOS":=^50}')
print(f"Qtde. de votos 1º canditado: {candito_1}")
print(f"Qtde. de votos 2º canditado: {candito_2}")
print(f"Qtde. de votos 4º canditado: {candito_3}")
print(f"Qtde. de votos 3º canditado: {candito_4}")
print(f"Total em porcentagem de votos nulos: {(nulo / total) * 100:.2f}%")
print(f"Total em procentagem de votos em branco: {(branco / total) * 100:.2f}%")
