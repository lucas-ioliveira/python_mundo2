'''
 Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
 No final do programa, mostre: a média de idade do grupo, qual é o nome
 do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
total_mulher_20 = 0
for pessoa in range(1, 5):
    print(f'---- {pessoa}° pessoa ----')
    nome = str(input('Qual o seu nome: ')).strip()
    idade = int(input('Qual sua idade: '))
    sexo = str(input('sexo [M/F]: ')).strip()
    soma_idade += 1
    if  pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mn' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher_20 += 1
media_idade= soma_idade / 4
print(f'A média de idade do grupo é de {media_idade:.2f} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_mais_velho}')
print(f'Ao todo são {total_mulher_20} mulheres com menos de 20 anos.')