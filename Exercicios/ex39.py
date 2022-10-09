'''
ALISTAMENTO MILITAR
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
# import referente a datas
from datetime import date

# Variáveis
ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
idade = ano_atual - ano_nascimento

print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}')

# Condições aninhadas.
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não tem 18 anos, ainda faltam {saldo} anos para o alistamento.')
    ano = ano_atual + saldo
    print(f'Seu alistamento será em {ano}.')

else:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos')
    ano = ano_atual - saldo
    print(f'Seu alistamento foi em {ano}.')
