'''
Progreção Aritmética.
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''
termo = int(input('1º termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print(f'{c}', end="-> ")

