while True:
    sexo = str(input("Sexo (M/F): ")).strip()

    if sexo in "Mm":
        print("Sexo Masculino correto")
        break
    elif sexo in "Ff":
        print("Sexo Feminino correto")
        break
    else:
        print("Opção inválida tente novamente...")
        continue