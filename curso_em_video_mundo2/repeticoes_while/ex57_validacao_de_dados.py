while True:
    sexo = str(input("Sexo (M/F): ")).strip().upper()[0]

    if sexo in "Mm":
        print("Sexo Masculino correto")
        break
    elif sexo in "Ff":
        print("Sexo Feminino correto")
        break
    else:
        print("Opção inválida tente novamente...")
        continue
print("FIM")

#outra forma 
sexo = str(input("Informe seu Sexo (M/F): ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Opção inválida. Informe seu Sexo (M/F): ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso.")