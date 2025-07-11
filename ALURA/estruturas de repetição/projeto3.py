faixa_0_25 = 0
faixa_26_50 = 0
faixa_51_75 = 0
faixa_76_100 = 0

while True:

    try:
        idade = int(input("Digite a idade do cliente (para encessar digite um valor negativo): "))

        if idade < 0:
            break
        else:
            if 0 <= idade <= 25:
                faixa_0_25 += 1
            elif 26 <= idade <= 50:
                faixa_26_50 += 1
            elif 51 <= idade <= 75:
                faixa_51_75 += 1
            elif 76 <= idade <= 100:
                faixa_76_100 += 1
            else:
                print("Idade fora do intervalor delimitada... Tente novamente")

    except ValueError:
        print("Valor não numérico inserido. Tente novamente...")

total = faixa_0_25 + faixa_26_50 + faixa_51_75 + faixa_76_100
print(25 * "-=")
print(f"{'DISTRIBUIÇÃO DE IDADES':.^50}")
print(f"Total de clientes analisados: {total}")
print(f"Total - faixa etária entre 0 e 25 anos: {faixa_0_25} pessoa(s) - {(faixa_0_25/total) * 100:.2f}%")
print(f"Total - faixa etária entre 26 e 50 anos: {faixa_26_50} pessoa(s) - {(faixa_26_50/total) * 100:.2f}%")
print(f"Total - faixa etária entre 51 e 75 anos: {faixa_51_75} pessoa(s) - {(faixa_51_75/total) * 100:.2f}%")
print(f"Total - faixa etária entre 76 e 100 anos: {faixa_76_100} pessoa(s) - {(faixa_76_100/total) * 100:.2f}%")
    

