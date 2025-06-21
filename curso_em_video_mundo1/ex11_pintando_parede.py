comprimento = float(input("Insira o compromimento da parede: "))
altura = float(input('Insira a altura da parede: '))
area = comprimento * altura
tinta =  area / 2
print(f"Sua parede tem a dimensão de {comprimento} x {altura} e sua área é de {area:.2f}m².")
print(f"Você precisa de {tinta}l de tinta.")