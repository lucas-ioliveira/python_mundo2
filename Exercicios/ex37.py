'''
CONVERSOR DE BASES.
Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário,
2 para octal e
3 para hexadecimal.
'''
# Variável
num = int(input('Digite um número inteiro: '))

# Opções a ser escolhida
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BONÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

# A opção que o usuário escolheu.
opcao = int(input('Sua Opção: '))

# condições aninhadas.
if opcao == 1:
    print(f'{num} convertido para BNÁRIO é igual a {bin(num)[2:]}.')

elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}.')

elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}.')

else:
    print(f'Opção invalida, tente novamente.')

