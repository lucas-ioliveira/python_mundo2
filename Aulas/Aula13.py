'''
Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro
o “for”, que é uma estrutura versátil e simples de entender.
'''
#exemplos
'''
for => para.
c => nome da variável de minha escolha. 
in => em.
range => intervalo. 
(0 ,6) => 6x 

for c in range(0, 6):
    print('OI.')

for c in range(1, 6):
    print('OI.')
'''
# Ex 2
'''
for c in range(0,6): #Vai gerear um contador de com 6 algoritimos do 0 à 5.
    print(c)
for c in range(1,6): #Vai gerear um contador de com 5 algoritimos do 1 à 5.
    print(c)
'''

# Ex 3
'''
for c in range(6, 0, -1): #Vai gerear um contador inverso de com 6 algoritimos do 6 à 1.
    print(c)
'''

# Ex 4
'''
for c in range(0, 7, 2): #Vai gerear um contador pulando de 2 em 2.
    print(c)
'''

# Ex 5
# Gera um contador com um núrero que o usuário digitou.
# n+1 => soma o ultimo número para que no  final do contador apareça o número que o usuário digitou.
'''
n = int(input('Digite um numero inteiro: '))
for c in range(0, n+1):
    print(c)
print('Fim!')
'''

# Ex 6
# Gera um contador pulando de 2 em 2
'''
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
'''
