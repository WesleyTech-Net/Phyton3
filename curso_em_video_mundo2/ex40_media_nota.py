nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media < 5:
    print(f"Sua média é de {media:.2f} pontos. VOCÊ ESTÁ REPROVADO!")
elif media >= 5 and media < 6.9:
    print(f"Sua média é de {media:.2f} pontos. VOCÊ ESTÁ DE RECUPERAÇÃO!")
else:
    print(f"Sua média é de {media:.2f} pontos. VOCÊ ESTÁ APROVADO!")