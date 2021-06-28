#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date
nascimento = int(input("Que ano nasceu o atleta? "))
atual = date.today().year
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação Mirim.')
elif idade <= 14:
    print('Classificação Infantil.')
elif idade <= 19:
    print('Classificação Júnior.')
elif idade <= 25:
    print('Classificação Sênior.')
else:
    print('Classificação Master.')