from datetime import date
contMaiorIdade = 0
contMenorIdade = 0
atual = date.today().year

for i in range(1, 6 + 1):
    ano = int(input(f"Em que ano a {i}º pessoa nasceu: "))
    idade = atual - ano
    print(idade)
    
    if idade < 18:
        contMenorIdade += 1        
    elif idade >= 18:
        contMaiorIdade += 1
        
print(f"Ao todo tivemos {contMenorIdade} menores de idade e {contMaiorIdade} maiores de idade. ")
       