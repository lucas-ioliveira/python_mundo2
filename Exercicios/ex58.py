'''
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
'''
from random import randint
print('========Jogo de advinhação========')
computador = randint(1, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que voê consegue advinhar qual foi?')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite: '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'O jogador acertou com {tentativas}, Parabéns!')
