'''
Contador.
Faça um programa que calcule a soma entre todos os números que são múltiplos
de três e que se encontram no intervalo de 1 até 500.
'''
s = 0
count = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        count = count + 1
        s = s + c
print(f'A soma de todos os {count} valores solicitados é {s}')