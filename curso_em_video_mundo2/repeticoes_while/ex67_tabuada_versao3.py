
while True:
    print(10 * "-=")
    tabuada = int(input("Qual tabuada você deseja: "))
    print(10 * "-=")
    if tabuada < 0:
        break
    for i in range(1, 11 ):
        print(f"{tabuada} * {i} = {tabuada * i}")

print("VOLTE SEMPRE!")