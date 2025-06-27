n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
print(10 * "=", "MENU", 10 * "=")
print("""
    [1] - SOMAR
    [2] - MULTPLICAR
    [3] - MAIOR
    [4] - NOVOS NÚMEROS
    [5] - SAIR DO PROGRMA 
      """)

while True:
    
    try:
        op = int(input("Escolha uma opção: "))

        if op == 1:
            soma = n1 + n2
            print(f"A soma entre {n1} e {n2} é igual a {soma}")
            escolha = int(input("Deseja novos números ou sair do programa? "))
            if escolha == 4:
                n1 = int(input("Primeiro valor: "))
                n2 = int(input("Segundo valor: "))
                print(10 * "=", "MENU", 10 * "=")
                print("""
                    [1] - SOMAR
                    [2] - MULTPLICAR
                    [3] - MAIOR
                    [4] - NOVOS NÚMEROS
                    [5] - SAIR DO PROGRMA 
                    """)
            elif escolha == 5:
                print("Tenha um excelente dia!")
                break

        elif op == 2:
            soma = n1 * n2
            print(f"A multiplicação entre {n1} e {n2} é igual a {soma}")

            escolha = int(input("Deseja novos números ou sair do programa? "))
            if escolha == 4:
                n1 = int(input("Primeiro valor: "))
                n2 = int(input("Segundo valor: "))
                print(10 * "=", "MENU", 10 * "=")
                print("""
                    [1] - SOMAR
                    [2] - MULTPLICAR
                    [3] - MAIOR
                    [4] - NOVOS NÚMEROS
                    [5] - SAIR DO PROGRMA 
                    """)
            elif escolha == 5:
                print("Tenha um excelente dia!")
                break


        elif op == 3:
            if n1 < n2:
                print(f"O maior número entre {n1} e {n2} é {n2}")
            else:
                print(f"O maior número entre {n1} e {n2} é {n1}")
            escolha = int(input("Deseja novos números ou sair do programa? "))
            n1 = int(input("Primeiro valor: "))
            n2 = int(input("Segundo valor: "))

            print(10 * "=", "MENU", 10 * "=")
            print("""
                [1] - SOMAR
                [2] - MULTPLICAR
                [3] - MAIOR
                [4] - NOVOS NÚMEROS
                [5] - SAIR DO PROGRMA 
                """)
        elif escolha == 5:
            print("Tenha um excelente dia!")
            break        
            
    except ValueError:
        print("Opção inválida. Tente novamente...")
        continue