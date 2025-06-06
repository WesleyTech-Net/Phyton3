print(10 * ' ', 'CLASSIFICAÇÃO DE TRIÂNGULO', 10 * ' ')
v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo valor: '))
v3 = float(input('Terceiro valor: '))

#preciso corrigir
if v1 == 0 or v2 == 0 or v3 == 0:
    print('ESSE TRIÂNGULO NÃO EXISTE!')
elif v1 + v2 < v3 and v1 + v3 < v2 and v3 + v2 < v1:
    print('ESSE TRIâNGULO NÃO EXISTE!')
elif v1 == v2 and v3 == v2:
    print('TRIÂNGULO EQUILÁTERO')
elif v1 != v2 and v2 != v1 and v3 != v1 and v3 != v2:
    print('TRIÂNGUKO ESCALENO')
else:
    print('TRIÂNGULO ISÓSCELES')
