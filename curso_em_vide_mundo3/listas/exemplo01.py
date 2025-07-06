teste = list()
teste.append("Gustavo")
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = "Wesley"
teste[1] = 32
galera.append(teste[:])
print(galera)