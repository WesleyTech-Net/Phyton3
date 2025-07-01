resposta = 'S'

soma = 0
contador = 0
media = 0
maior = 0 
menor = 0

while resposta in 'Ss':

    try:
        num = int(input("Digite um número: "))
        soma +=  num
        contador += 1
        
        if contador == 1:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            elif num < maior:
                menor = num

        resposta = str(input("Quer continuar (S/N)? ")).strip().upper()[0]
    except ValueError:
        print("Opção inválida. Tente novamente...")
        continue
media = soma / contador
print(f"A soma entre o valores é igual a {soma}.\nA media entre eles é igual a {media}")
print(f"A maior valor é {maior} o menor valor é {menor}")
