import math
angulo = float(input("Insira o ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f"O ângulo de {angulo} tem o SENO de {seno:.2f}\nO ângulo de {angulo} tem o COSSENO de {cosseno:.2f}\nO ângulo de {angulo} tem a TANGENTE de {seno:.2f} ")