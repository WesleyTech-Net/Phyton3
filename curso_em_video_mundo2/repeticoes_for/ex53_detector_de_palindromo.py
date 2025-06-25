frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
juntar = "".join(palavras)
inverso = ""


for i in range (len(juntar) - 1, -1, -1):
    inverso += juntar[i]
print(f"O inverso de {frase} é {inverso}")
if inverso == juntar:
    print("Temos um palíndromo!")
else:
    print("Não temos um palíndromo!")