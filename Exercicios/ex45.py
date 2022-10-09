'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
# Biblioteca para números aletatórios
from random import randint
# Biblioteca para criar um temporizador.
from time import sleep

# Nome do jogo
jogo = 'Jokenpô'
print(f'{jogo:=^30}')

# Opções para o jogador
print('''Escolha uma opção.
[1- Pedra] 
[2- Papel] 
[3- Tesoura]
''')
jogador = int(input('Qual a sua jogada? '))
print('Jo')
sleep(1)
print('ken')
sleep(1)
print('pô!')

# Variáveis
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(1,3)

print('=' * 30)
print()
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print()
print('=' * 30)

# Condições aninhadas
if computador == 1: # computador jogou pedra.
    if jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador Venceu!')
    elif jogador == 3:
        print('Computador Venceu!')
    else:
        print('Jogada inválida.')
elif computador == 2: # computador jogou papel.
    if jogador == 1:
        print('Computador Venceu!')
    elif jogador == 2:
        print('Empate!')
    elif jogador == 3:
        print('Jogador Venceu!')
    else:
        print('Jogada inválida.')
elif computador == 3: # computador jogou tesoura.
     if jogador == 1:
        print('Jogador Venceu!')
     elif jogador == 2:
        print('Computador Venceu!')
     elif jogador == 3:
        print('Empate!')
     else:
        print('Jogada inválida.')
else:
    print('Digite uma opção válida!')
