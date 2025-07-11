while True:

    try:
        numero = int(input("Digite um número para saber se ele é primo ou não: "))

        if numero < 2:
            primo = False
        else:
            primo = True
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    primo = False
                    break
        if primo:
            print(f"O {numero} é um número PRIMO!")
        else:
            print(f"O {numero} não é um número PRIMO!")

        op = str(input("Deseja verifcar se outro número é primo (S/N): ")).strip().upper()[0]
        if op == "N":
            break
    except ValueError:
        print("🛑 Valor não numérico não inserido. Tente novamente...")

print("ENCERRANDO O PROGRAMA...")