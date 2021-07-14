#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

P1 = float(input('Qual nota você tirou na prova 1? '))
P2 = float(input('Qual nota você tirou na prova 2? '))
Média = (P1+P2)/2
if Média < 5:
    print('Você foi reprovado! Sua média foi de {}.'.format(Média))
elif Média >=5 and Média <= 6.9:
    print('Você está de recuperação! Sua média foi de {}.'.format(Média))
else:
    print('Você foi aprovado! Sua média foi de {}.'.format(Média))
