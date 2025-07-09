#1) Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.
num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))

if num1 > num2 :
    print(f"O número {num1} é maior que {num2}")
else:
    print(f"O número {num2} é maior que {num1}")

#2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).
producao_anterior = float(input("Quanto a empresa produziu no mês anterior? R$ "))
producao_atual = float(input("Quanto a empresa produziu no mês atual: R$ "))
diferenca = producao_atual - producao_anterior
divisao = diferenca / producao_anterior
percentual = divisao * 100

if percentual > 0:
    print(f"A Empresa obteve um crescimento de {percentual:.1f} %")
else:
    print(f"A Empresa obteve um decrescimento de {percentual:.1f} %")   

#3) Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
letra = str(input("Escolha letra: ")).strip().upper()[0]
if letra in "AEIOU":
    print(f'A letra "{letra}" é uma VOGAL.')
else:
     print(f'A letra "{letra}" é uma CONSOANTE.')

#4) Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.
carro = str(input("\nInsira o modelo do carro: ")).strip().upper()
ano1 = float(input("Primeiro valor: R$ "))
ano2 = float(input("Segundo valor: R$ "))
ano3 = float(input("Terceiro valor: R$ "))
preco_medio = (ano1 + ano2 + ano3) / 3
print(f"O preço médio do carro {carro} nos três anos consecutivos é igual a R$ {preco_medio:.2f}")

if ano1 > ano2 and ano1 > ano3:
    print(f"O valor mais alto foi do primeiro ano: R$ {ano1}")
elif ano2 > ano1 and ano2 > ano3:
    print(f"O valor mais alto foi do segundo ano: R$ {ano2}")
else:
     print(f"O valor mais alto foi do terceiro ano: R$ {ano3}")

#5) Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
produto1 = float(input("\nPreço do primeiro produto: R$ "))
produto2 = float(input("Preço do segundo produto: R$ "))
produto3 = float(input("Preço do terceiro produto: R$ "))

if produto1 < produto2 and produto1 < produto3:
    print(f"O primeiro produto é o mais barato: R$ {produto1:.2f}")
elif produto2 < produto1 and produto2 < produto3:
    print(f"O segundo produto é o mais barato: R$ {produto2:.2f}")
else:
     print(f"O terceiro produto é o mais barato: R$ {produto3:.2f}")

#6) Escreva um programa que leia três números e os exiba em ordem decrescente.
num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
num3 = int(input("Terceiro valor: "))

if num1 >= num2 and num2 >= num3:
    print(num1, num2, num3)
elif num1 >= num3 and num3 >= num2:
    print(num1, num3, num2)
elif num2 >= num1 and num1 >= num3:
    print(num2, num1, num3)
elif num2 >= num3 and num3 >= num1:
    print(num2, num3, num1)
elif num3 >= num1 and num1 >= num2:
    print(num3, num1, num2)
else:
    print(num3, num2, num1)

#7) Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.
turno = str(input("Qual turno você estuda (manhã/tarde/noite)? "))
turno = turno.replace(" ", "").upper() #retira todos os espaços 

if turno == "MANHÃ":
    print("Bom dia!")
elif turno == "TARDE":
    print("Boa Tarde!")
elif turno == "NOITE":
    print("Boa noite!")
else:
    print("Valor inválido!")

#8) Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.
numero = int(input("Escolha um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é PAR!")
else:
    print(f"O número {numero} é ÍMPAR!")

#9) Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.

numero = input("Escolha um número: ")
valor = float(numero)

if valor.is_integer():
    print(f"O número {numero} é um inteiro")
else:
    print(f"O número {numero} é decimal")