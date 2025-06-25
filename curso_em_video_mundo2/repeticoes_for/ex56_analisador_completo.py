somaIdade = 0
idadeMaiorMasculino = 0
nomeMaisVelho = ''
idadeMenorFeminino = 0
contMulher = 0
for i in range (1, 5):
    print(5 * "-", f"{i}ª PESSOA", 5 * "-" )
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo (M/F): ")).strip()

    #condição para saber qual homem é o mais velho e mostrar o nome desse homem mais velho.
    if i == 1 and sexo in "Mm":
        idadeMaiorMasculino = idade
        nomeMaisVelho = nome
    if sexo in 'Mm' and idade > idadeMaiorMasculino:
        idadeMaiorMasculino = idade
        nomeMaisVelho = nome
    
    #condição para contar quantas mulheres tem menos de 20 anos de idade.
    if sexo in "Ff" and idade < 20:
        contMulher += 1

    #média de idade das pessoas
    somaIdade += idade
    mediaIdade = somaIdade / i


print(f"A média de idade do grupo é de {int(mediaIdade)} anos.")
print(f"O home mais velho se chama {nomeMaisVelho} e tem {idadeMaiorMasculino} anos de idade.")
print(f"São {contMulher} mulheres com menos de 20 anos de idade.")


