'''
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo
com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
'''
# import referente a data.
from datetime import date

# Variáveis
ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_nascimento

print(f'A idade do atleta é: {idade} anos.')

# Condições aninhadas.
if idade <= 9:
    print(f'A categoria do atleta é: MIRIM')

elif idade > 9 and idade <= 14:
    print(f'A categoria do atleta é: INFANTIL.')

elif idade > 14 and idade <= 19:
    print(f'A categoria do atleta é: JÚNIOR.')

elif idade > 19 and idade <= 25:
    print(f'A categoria do atleta é: SÊNIOR.')

else:
    print(f'A categoria do atleta é: MASTER.')