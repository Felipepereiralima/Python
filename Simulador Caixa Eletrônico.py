#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('=' * 50)
print('{:^50}'.format('BANCO LIMA'))
print('=' * 50)
sacado = int(input('{:^40}'.format('Qual o valor a ser sacado? R$')))
total = sacado
cédula = 50
totalCédula = 0
while True:
    if total >= cédula:
        total -= cédula
        totalCédula += 1
    else:
        if totalCédula >0:
            print('{:^40}'.format('Total de {} cédulas de R$ {:.2f}'.format(totalCédula, cédula)))
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totalCédula = 0
        if total == 0:
            break
print('=' * 50)
print('{:^50}'.format('Volte sempre ao Banco Lima!'))
