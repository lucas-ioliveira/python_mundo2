'''
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''
# maior e menor peso.
maior = 0
menor = 0

for pessoa in range(1, 6):
    peso = float(input(f'Digite o valor do peso da {pessoa}° pessoa: '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior:.2f}kg.')
print(f' Omenor peso lido foi de {menor:.2f}Kg.')
