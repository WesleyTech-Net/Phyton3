#Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.
frase = "Só sei que nada sei."
print(frase)

#Crie um código que solicite uma frase e depois imprima a frase na tela.
frase = str(input("1 Digite uma frase: "))
print(frase)

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.
frase = str(input("2 Digite uma frase: ")).upper()
print(frase)

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.
frase = str(input("3 Digite uma frase: ")).lower()
print(frase)

#Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.
frase = "    Só sei que nada sei   "
print(frase.strip())

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.
frase = str(input("4 Digite uma frase: ")).strip()
print(frase)

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
frase = str(input("5 Digite uma frase: ")).strip().lower()
print(frase)

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.
frase = str(input("6 Digite uma frase: ")).strip().lower()
print(frase.replace('e', 'f'))

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
frase = str(input("7 Digite uma frase: ")).strip().lower()
print(frase.replace('a', '@'))

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
frase = str(input("7 Digite uma frase: ")).strip().lower()
print(frase.replace('s', '$'))