print(15 * "-=")
print("Analisador de triângulos")
print(15 * "-=")

s1 = float(input("Primeiro segmento: "))
s2 = float(input("Segundo segmento: "))
s3 = float(input("Terceiro segmento: "))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("Os seguimentos acima formam um triângulo!")
else:
    print("Os seguimentos acima não forma um triângulo!")