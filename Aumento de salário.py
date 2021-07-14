#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
Salario = float(input('Qual o seu salário? '))
if Salario <= 1250:
    A = (Salario*15)/100 + Salario
    print('O seu salário teve aumento de 15% e ficou em R${:.2f}.'.format(A))
else:
    B = (Salario*10)/100 + Salario
    print('O seu salário teve um aumento de 10% e ficou em R${:.2f}.'.format(B))
