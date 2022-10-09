'''
Desenvolva um programa que leia seis números inteiros e mostre
a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''
s = 0
c = 0
for n_i in range(1, 7):
    n = int(input(f'Digite o {n_i}° valor: '))
    if n % 2 == 0:
        s = s + n
        c = c + 1
print(f'Você informou {c} números e a soma foi {s}.')


