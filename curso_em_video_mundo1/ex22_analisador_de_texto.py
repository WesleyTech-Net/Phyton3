import time
nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
time.sleep(2)
print(f"Seu nome em maísculas fica {nome.upper()}")
print(f"Seu nome em minúsculas fica {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome)-nome.count(' ')}")
print(f"Seu primeiro nome tem {nome.find(' ')} letras.")