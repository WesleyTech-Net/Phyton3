#10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa
#usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre
#o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

#pedido para o usário inserir os dois valores
numero1 = float(input("Primeiro valor: "))
numero2 = float(input("Segundo valor: "))

#analisando o primero valor

print(f"{'[ANÁLISE DO PRIMEIRO VALOR]':-^50}")
if numero1 % 2 == 0:
    print("\nO valor é PAR!")
else:
    print("O valor é ÍMPAR!")
if numero1 > 0:
    print("O valor é positivo")
else:
    print("O valor é negativo")
if numero1.is_integer():
    print("O valor é inteiro\n")
else:
    print("O valor é decimal\n")

#analisando o segundo valor]
print(f"{'[ANÁLISE DO SEGUNDO VALOR]':-^50}")
if numero2 % 2 == 0:
    print("O primeiro valor é PAR!")
else:
    print("O primeiro valor é ÍMPAR!")
if numero2 > 0:
    print("O valor é positivo")
else:
    print("O valor é negativo")
if numero2.is_integer():
    print("O valor é inteiro\n")
else:
    print("O valor é decimal\n")