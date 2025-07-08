from time import sleep

lista_funcionarios = list()
id_global = 1021927

print("BEM VINDO A EMPRESA DE WESLEY SAMPAIO")

#função para cadastrar funcionário
def cadastrar_funcionario(id):
    print(10 * "-","MENU CADASTRAR FUNCIONÁRIO", 10 * "-")
    print(f"ID do funcionário: {id_global}")
    nome = str(input("Por favor entre com o Nome do Funcionário: ")).strip()
    setor = str(input("Por favor entre com o Setor do Funcionário: ")).strip().lower()
    salario = float(input("Por favor entre com o Salário do funcionário: "))

    funcionario = {"id": id, "nome": nome, "setor":setor, "salario":salario}
    lista_funcionarios.append(funcionario.copy())


#função para consultar funcionário
def consultar_funcionario():

    #menu para consultar os funcionários 
    while True:
        print(17 * "-", "MENU CONSULTAR FUNCIONÁRIO", 17 * "-")
        print("""Escoha a opção desejada:
        [1] - Consultar Todos os Funcionários
        [2] - Consultar Funcionário por id
        [3] - Consultar Funcionário(s) por Setor
        [4] - Retornar""")
        try:
            opcao_consultar = int(input(">> "))

            #condição de parada caso o usário escolha a opção 4
            if opcao_consultar == 4:
                break
            else:
                #condição para consultar todos os funcionário caso o usuário escolha a opção 1
                if opcao_consultar == 1:
                    print(10 * "-")
                    if not lista_funcionarios:
                        print("Funcioário não cadastrado")
                    else:
                        for func in lista_funcionarios:
                            print(f"id: {func["id"]}")
                            print(f"Nome: {func["nome"]}")
                            print(f"Setor: {func["setor"]}")
                            print(f"Salário: {func["salario"]:.1f}\n")
                
                #condição para consultar o funcionário por ID caso o usuário escolha a opção 2
                elif opcao_consultar == 2:
                    try:
                        buscar_por_id = int(input("Digite o id do funcionário: "))
                        encontrado = False
                        for func in lista_funcionarios:
                            if func["id"] == buscar_por_id:
                                print(f"id: {func["id"]}")
                                print(f"Nome: {func["nome"]}")
                                print(f"Setor: {func["setor"]}")
                                print(f"Salário: {func["salario"]:.1f}\n")
                                encontrado = True
                            
                        if not encontrado:
                            print(f"ID: {buscar_por_id}, não encontrado. Tente novamente...")
                            continue                                
                    except ValueError:
                        print("OPÇÃO INVÁLIDA! Tente novamente...")
                
                #condição para consultar o funcionário por SETOR caso o usuário escolha a opção 3
                elif opcao_consultar == 3:
                    try:
                        buscar_setor = str(input("Digite o setor do(s) funcionário(s): ")).strip().lower()
                        setores_encontrados = []

                        for setores in lista_funcionarios:
                            if setores["setor"].strip().lower() == buscar_setor:
                                setores_encontrados.append(setores)

                        if setores_encontrados:
                            for setores in setores_encontrados:
                                print(f"id: {setores["id"]}")
                                print(f"Nome: {setores["nome"]}")
                                print(f"Setor: {setores["setor"]}")
                                print(f"Salário: {setores["salario"]:.1f}\n")
                        else:
                            print("Não foi encontrado nenhum funcionário nesse setor. Tente novamente")
                            continue
                    except ValueError: 
                         print("OPÇÃO INVÁLIDA! Tente novamente...")    
                
        except ValueError:
            print("Opção Inválida.")

#função para remover funcionário
def remover_funcionario():
    while True:
        print(17 * "-", "MENU REMOVER FUNCIONÁRIO", 17 * "-")
        try:
            remover = int(input("Digite o id do funcionário a ser removido: "))
            encontrado = False
            
            for rem in lista_funcionarios:
                if rem["id"] == remover:
                    lista_funcionarios.remove(rem)
                    print("Funcionário removido com sucesso!")
                    encontrado = True
                    break

            if encontrado:
                break
            else:
                print("ID inválido. Tente novamente...")
                    
        except ValueError:
            print("Opção inválida. Tente novamente...")


#Programa principal
while True:

    #menu de escolha para o usuário
    print(50 * "-")
    print(17 * "-", "MENU PRINCIPAL", 17 * "-")
    print("""Escolha a opção desejada:
      [1] - Cadastrar Funcionário
      [2] - Consultar Funcionário(s)
      [3] - Remover Funcionário
      [4] - Sair""")
    
    opcao = int(input(">> "))

    #condição de parada caso o usário escolha a opção 4
    if opcao == 4:
        print("Encerrando o programa...")
        sleep(2)        
        break
    else:
    #condição para cadastrar o funcionário caso o usuário escolha a opção 1    
        if opcao == 1:
            cadastrar_funcionario(id_global)
            id_global += 1
        
    #condição para consultar os funcionários caso o usuário escolha a opção 2
        elif opcao == 2:
            consultar_funcionario()
        
        elif opcao == 3:
            remover_funcionario()
    
        continue