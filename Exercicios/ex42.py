'''
TRIÂNGULO
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
'''
# Variáveis
r1 = float(input('Digite o valor da 1° segmento: '))
r2 = float(input('Digite o valor da 2° segmento: '))
r3 = float(input('Digite o valor da 3° segmento: '))

# Condições aninhadas
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um trinângulo,', end=" ")
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('OSÓSCELES!')
else:
    print('Os segmentos acima não podem formar um triângulo.')

