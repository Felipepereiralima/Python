#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais
valor = int(input('Digite um número: '))
valor2 = int(input('Digite outro número: '))
if valor > valor2:
    print('O primeiro valor é maior que o segundo.')
elif valor < valor2:
    print('O segundo valor é maior que o primeiro.')
else:
    print('Não existe valor maior, os dois são iguais.')
