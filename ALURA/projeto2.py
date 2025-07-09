print(f'{"ANALISADOR DE TRIÂNGULOS":-^50}')

segmento1 = int(input("Primeiro segmento: "))
segmento2 = int(input("Segundo segmento: "))
segmento3 = int(input("Terceiro segmento: "))

if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    print("Os segmentos acima formam um triângulo!")
    if segmento1 == segmento2 == segmento3:
        print("✅ TRIÂNGULO EQUILÁTERO")
    elif segmento1 != segmento2 != segmento3 != segmento1:
        print("✅ TRIÂNGULO ESCALENO")
    else:
        print("✅ TRIÂNGULO ISOSCELES")
else:
    print("🛑 -- ATENÇÃO -- 🛑")
    print('Os segmentos acima não formam um triângulo!')
