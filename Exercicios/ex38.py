'''
NÚMERO MAIOR.
Escreva um programa que leia dois números inteiros e compare-os.
mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais
'''
# Variáveis
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

# Condições aninhadas.
if num1 > num2:
    print('O primeiro valor é maior.')

elif num1 < num2:
    print('O segundo valor é maior')

elif num1 == num2:
    print('Não exite valor maior, os dois são iguais.')

else:
    print('Digite um número inteiro.')