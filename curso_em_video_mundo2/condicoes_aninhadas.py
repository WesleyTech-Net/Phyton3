nome = str(input("Qual é o seu nome? ")).strip().upper()

if nome == "GUSTAVO":
    print("Que nome bonito!")

elif nome == "WESLEY" or nome == "NATHALYE" or nome == "VICTOR":
    print("Seu nome é bem popular no Brasil!")
elif nome in "ANA" or nome in "JULIA" or nome in "LETÍCIA":
    print("Belo nome feminino")
    
else:
    print("Seu nome é bem normal!")

print(f'Tenha um bom dia {nome}!')