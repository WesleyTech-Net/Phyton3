num = int(input("Insira um número inteiro: "))
print("\nEscolha uma das opções abaixo: ")
print("[1] - converter para BINÁRIO")
print("[2] - converter para HEXADECIMAL")
print("[3] - converter para OCTAL")
opcao = int(input('\nSua opção: '))


if opcao == 1:
    print(f"O número {num} para BINÁRIO é igual a: {bin(num)[2:]}")
elif opcao == 2:
    print(f"O número {num} para BINÁRIO é igual a: {hex(num)[2:]}")
elif opcao == 3:
    print(f"O número {num} para BINÁRIO é igual a: {oct(num)[2:]}")
else:
    print("Opção inválida. Tente novamente...")