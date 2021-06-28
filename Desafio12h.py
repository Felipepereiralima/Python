#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
peso = float(input('Qual é o peso em Kg? '))
altura = float(input('Qual a sua altura em metros? '))
imc = peso / (altura **2)
print('O seu IMC é de {:.1f} '.format(imc), end='')
if imc < 18.5:
    print('você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('você está com sobrepeso.')
elif imc >=30 and imc <= 40:
    print('você está com obesidade.')
else:
    print('você está com obesidade mórbida.')
