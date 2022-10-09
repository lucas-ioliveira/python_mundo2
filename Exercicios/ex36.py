'''
Emprestimo.
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será
negado.
'''
# Variáveis
casa = float((input('Digite o valor do imovel:R$')))
salario = float(input('Digite o valor do seu salário:R$'))
anos = int(input('Em quantos anos pretende finaciar o imóvel: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print(f'Para pagar uma casa de R${casa:.2f} reais, em {anos} anos', end=" ")
print(f'A prestação será de R$ {prestacao:.2f}')

# Condições aninhadas.
if prestacao <= minimo:
    print('Emprestimo pode ser concedido!')

else:
    print('Emprestimo negado!')