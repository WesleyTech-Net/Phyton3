#verifica se a cidade tem Santo no nome
cidade = str(input("Qual sua cidade de nascimento? ")).strip()
print(cidade[:5].upper() == 'SANTO')
