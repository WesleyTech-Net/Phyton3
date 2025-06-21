def valid_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def existe_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, "wt+")
        a.close()
    except:
        print("Erro na criação do arquivo")
    else:
        print(f"Arquivo {nomeArquivo} criado com sucesso!\n")



#Programa Principal

arquivo = 'Funcionarios'
if existe_arquivo(arquivo):
    print('Arquivo Localizado no computador')
else:
    print('Arquivo inexistente')
    criar_arquivo

print("Bem vindo a Empresa de Wesley Sampaio")
print(50 * "-")
lista_fucionarios = []
id_global = 1021927

while True:
    print(22 * '-','MENU PRINCIPAL', 22 * '-')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Funcionário')
    print('2 - Consultar Funcionário')
    print('3 - Remover Funcionário')
    print('4 - Encerrar o Programa')
    escolha = valid_int(">>", 1, 4)
    if escolha == 1:
        cadastrar_funcionario()
    if escolha == 4: #SAIR DO PROGRAMA
        break



