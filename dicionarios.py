food = ("Laranja", "Lasanha", "Bacon", "Macarrão")
print("Tupla: ", food)


food = ["Laranja", "Lasanha", "Bacon", "Macarrão"]
print("Lista: ", food)


food = {"Laranja", "Lasanha", "Bacon", "Macarrão"}
print("DICIONÁRIO: ", food)

#exemplo
info = {'nome':'Wesley', 'idade':32, 'profissão':'Desenvolvedor Python'}
print(info)
print(info['nome'])
print(info['idade'])
print(info['profissão'])

print(info.values())
for valeus in info.values():
    print(valeus)


print(info.keys())
for keys in info.keys():
    print(keys)

print(info.items())
for keys, valeus in info.items():
    print(f'{keys} = {valeus}')
