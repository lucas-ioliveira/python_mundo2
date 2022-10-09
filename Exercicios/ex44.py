'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
'''
# Apliquei conhecimentos adiquiridos e apliquei no exercio, fiz algo a mais do que foi pedido.
from time import sleep

nome_loja = 'LOJAS BESERRA DE OLIVEIRA'
print(f'{nome_loja:=^40}')

# Variáveis
nome = str(input('Digite o seu nome: ')).upper()
produto = float(input('Valor do produto R$ '))

# Opções para o usuário
print('''Informe a forma de pagamento:
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal 
[4] 3x ou mais no cartão: 20% de juros''')

print()

opcao = int(input('Digite a opção escolhida: '))
print('PROCESSANDO...')
sleep(2)
print()

# Condições aninhadas
if opcao == 1:
    dinheiro_cheque = produto - (produto * 10 / 100)
    print(f'De acordo com a forma de pagamento\n'
          f'o(a) Sr(a) terá 10% de desconto e\n'
          f'pagará pelo produto o valor de\n'
          f'R$ {dinheiro_cheque:.2f} à vista\n'
          f'ou em cheque.')

elif opcao == 2:
    avista_cartao = produto - (produto * 5 / 100)
    print(f'De acordo com a forma de pagamento\n'
          f'o(a) Sr(a) terá 5% de desconto e\n'
          f'pagará pelo produto o valor de\n'
          f'R$ {avista_cartao:.2f} à vista\n'
          f'no cartão.')

elif opcao == 3:
    parcelado2x = produto / 2
    print(f'De acordo com a forma de pagamento\n'
          f'o(a) Sr(a) pagará pelo produto o\n'
          f'valor de R$ {produto:.2f} parcelado\n'
          f'em 2x o valor de R$ {parcelado2x:.2f} no cartão.')

elif opcao == 4:
    parcelado3x = produto + (produto * 20 / 100)
    num_parcelas = int(input('Digite em quantas parcelas deseja: '))
    total = parcelado3x / num_parcelas
    print(f'De acordo com a forma de pagamento\n'
          f'o(a) Sr(a) pagará pelo produto com '
          f'acrecimo de 20% valor de R$ {parcelado3x:.2f} reais,\n'
          f'porém parcelado em {num_parcelas}x no cartão de crédito\n'
          f'o valor de R$ {total:.2f} reais.')

else:
    print('Digite uma opção válida!')

print()
print(f'obrigado, e volte sempre {nome}! ')