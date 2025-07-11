from time import sleep

cont = 1
while True:

    try:
        
        numero = int(input("Escolha um número para exibir sua tabuada: "))
        
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
            cont += 1
        op = str(input("Deseja continuar (S/N): ")).strip().upper()[0]

        if op == "N":
            break

    except ValueError:
        print("Valor não numérico inserido. Tente novamente...")

print("ENCERRANDO O PROGRAMA...")
sleep(2)