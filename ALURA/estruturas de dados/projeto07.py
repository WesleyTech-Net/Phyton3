salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]

abonos = {}

#esse laço pega todos os itens da lista salarios e adiciona ao dicionario abonos
# calculando o acrescimo de 10% porém não inferior a 200.
for salario in salarios:
    abono = (salario * 10) / 100
    if abono < 200:
        abono = 200
    abonos[salario] = abono

print("Relação dos sálarios e abonos: ")
#esse laço separa de forma organizada os salarios com seus respectivos abonos.
for salario, abono in abonos.items():
    print(f"Salário: R$ {salario} - Abono: R$ {round(abono, 2)}")

print(40 * "-")
total_gastos = sum(abonos.values())
print(f"Total gasto com os abonos: R$ {round(total_gastos, 2)}")

maior_abono = max(abonos.values())
print(f"Maior valor de abono: R$ {round(maior_abono)}")

quantidade_abono_minio = list(abonos.values()).count(200)
print(f"Quantidade de colaborades que receberam o abono mínimo: {quantidade_abono_minio} colaboradores. ")