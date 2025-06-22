from random import randint
import time

print(13 * "-=--")
print("Vou pensar em número entre 0 e 5. Tente adivinhar")
print(13 * "-=--")

j = int(input("Em que número eu pensei? "))

print("PROCESSANDO...")
time.sleep(2)

computador = randint(0, 5)
if j == computador:
    print(f"Parabéns você acertou! Eu pensei no número {computador}")
else:
    print(f"Não foi dessa vez eu pensei no número {computador}!")
