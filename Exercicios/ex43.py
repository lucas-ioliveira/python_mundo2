'''
IMC
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
'''
# Variáveis
peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite a sua altura (m): '))
imc = peso / (altura ** 2)

print(f'De acordo com seu peso {peso:.2f} km e sua altura {altura:.2f} m,', end=" ")
print(f'o seu IMC é {imc:.2f},', end=" ")

# Condições aninhadas
if imc < 18.5:
    print('Abaixo do Peso')

elif imc == 18.5 and imc <= 25:
    print('Peso Ideal!')

elif imc <= 30:
    print('Sobrepeso!')

elif imc <= 40:
    print('Obesidade!')

else:
    print('Obesidade morbida, cuidado!')