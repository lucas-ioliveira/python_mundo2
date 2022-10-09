'''
 Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos.
'''
print('Gerador de progressão aritmética.')
print('-=' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} ->', end=" ")
        contador += 1
        termo += razao
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')