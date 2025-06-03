preco = float(input('Insira o valor do produto: '))
percentual = float(input('Insira o desconto do produto: '))
desconto = preco * percentual / 100
valorfinal = preco - desconto 
print(f'O valor R${preco} do produto terá um desconto de {desconto}%, ficando no valor total de R${valorfinal}')