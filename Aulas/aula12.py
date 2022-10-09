'''
Condições aninhadas
Nessa aula, vamos aprender como criar estruturas condicionais aninhadas,
usando os comandos if.. elif.. else em programas Python.
'''
# Exemplo
nome = str(input('Qual o seu nome? '))
if nome == 'Lucas':
    print('Que nome bonito!')
elif nome == 'Antônio' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é bem comum!')
print(f'Tenha um bom dia, {nome}!')
