'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles
(desconsiderando o flag).
'''
# Obs: Se ler o número fora e dentro do laço ele desconsidera o flag.
num = count = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    count += 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {count} números e a soma entre eles foi {soma}.')
