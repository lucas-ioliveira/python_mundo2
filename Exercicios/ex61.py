'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10
primeiros termos da progressão usando a estrutura while.'''

print('Gerador de progressão aritmética.')
print('-=' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1

while contador <= 10:
    print(f'{termo} ->', end=" ")
    contador += 1
    termo += razao
print('Fim.')