galera = list()
dado = list()
total_maior_idade = 0
total_menor_idade = 0
for i in range(0, 2):
    dado.append(str(input("Nome: ")).strip())
    dado.append(int(input("idade: ")))
    galera.append(dado[:])
    dado.clear()

for i in galera:
    if i[1] >= 20:
        print(f"{i[0]} é maior de idade.")
        total_maior_idade += 1
    else:
        print(f"{i[0]} é menor de idade")
        total_menor_idade += 1

print(f"Temos {total_maior_idade} maiores e {total_menor_idade} menores de idade")