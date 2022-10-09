'''
MÉDIA ESCOLAR
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
'''
# Variáveis
nota1 = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))
media = (nota1 + nota2) / 2

print(f'A sua 1° nota é {nota1} e a 2° nota é {nota2} e sua média é {media}')

# Condições aninhadadas.
if media >= 7:
    print('APROVADO.')

elif media <= 5:
    print('REPROVADO.')

elif media > 5 and media <= 6.9:
    print('RECUPERAÇÃO.')

