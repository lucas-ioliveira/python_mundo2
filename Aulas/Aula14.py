'''
While (enquanto) - estruturade repetição com teste lógico
'''
'''
# Ex
c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

# Ex 2

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('fim')
'''
# Ex 3
n = 1
par = 0
impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números par e {impar} números impar.')