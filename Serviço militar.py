#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
nascimento = int(input('Qual o seu ano de nascimento? '))
atual = date.today().year
idade = atual - nascimento
if idade == 18:
    print('Está na hora de se alistar!')
elif idade > 18:
    idades = idade - 18
    print('Já passou do tempo de se alistar, ja se passaram {} anos!'.format(idades))
else:
    idades2 = nascimento + 18
    print('Você não tem a idade necessária pra se alistar, seu alistamento será em {}.'.format(idades2))
