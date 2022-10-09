'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:
'''
frase = str(input('Digite uma frase:' )).strip().upper() # eliminei os espaços antes e depois e deixei s letras todas maísculas
palavra = frase.split() # gerar uma lista
junto = ''.join(palavra) # Juntei em uma string só.
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palídromo !')