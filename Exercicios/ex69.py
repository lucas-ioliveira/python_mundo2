'''
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o
usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''
total_18 = total_homens = total_mulheres_20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        total_18 += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        total_mulheres_20 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total_18}')
print(f'Ao todo temos {total_homens} homens cadastrados.')
print(f'E temos {total_mulheres_20} mulheres com menos de 20 anos.')
