times_brasileirao = [
  "Flamengo",
  "Cruzeiro",
  "RB Bragantino",
  "Palmeiras",
  "Bahia",
  "Fluminense",
  "Atlético-MG",
  "Botafogo",
  "Mirassol",
  "Corinthians",
  "Grêmio",
  "Ceará",
  "Vasco",
  "São Paulo",
  "Santos",
  "Vitória",
  "Internacional",
  "Fortaleza",
  "Juventude",
  "Sport"
]
print(20 * "-=")
print(10 * "-+", "CAMPEONATO BRASILEIRO", 10 * "-+")
cont = 1
for i in times_brasileirao:
    print(f"{cont}º lugar: {i}")
    cont += 1

print(20 * "-=")
print("Os 5 primeiros colocados são: \n")
for  i in range(5):
    print(f"{i+1}º colocado: {times_brasileirao[i]}")

print(20 * "-=")
print("Os 4 últimos colocados são: \n")
for  i in range(16, 20):
    print(f"{i+1}º colocado: {times_brasileirao[i]}")

print(20 * "-=")
print("Favorito a ganhar o campeonato:", end=" ")
for  i in range(1):
    print(f"{times_brasileirao[i].upper()}")

