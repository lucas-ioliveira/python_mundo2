'''
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
v = 0 #Variável referente a quantidade de vitórias
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total {total}')
    print('Deu par.' if total % 2 == 0 else 'Deu ímpar.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v =+ 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente? ')
print(f'GAME OVER! Você venceu {v} vezes.')


