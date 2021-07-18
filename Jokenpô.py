#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import randint
print('''Escolha entre:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
pc = int(randint(1, 3))
while True:
    opção = int(input('Digite a sua escolha [1/2/3]: '))
    if opção == 1:
        print('Você escolheu Pedra.')
        print('Pedra, ', end='')
        sleep(1)
        print('Papel, ', end='')
        sleep(1)
        print('Tesoura!')
        sleep(1)
        print('-=' * 22)
        if opção == 1 and pc == 2:
            print('Você perdeu! O computador escolheu papel.')
        elif opção == 1 and pc == 3:
            print('Você ganhou! O computador escolheu tesoura.')
        elif opção == 1 and pc == 1:
            print('Empate! Ambos escolheram pedra.')
    print('-=' * 22)
    if opção == 2:
        print('Você escolheu Papel.')
        print('Pedra, ', end='')
        sleep(1)
        print('Papel, ', end='')
        sleep(1)
        print('Tesoura!')
        sleep(1)
        print('-=' * 22)
        if opção == 2 and pc == 1:
            print('Você ganhou! O computador escolheu pedra.')
        elif opção == 2 and pc == 2:
            print('Empate! Ambos escolheram papel.')
        elif opção == 2 and pc == 3:
            print('Você perdeu! O computador escolheu tesoura.')
            print('-=' * 22)
    if opção == 3:
        print('Você escolheu Tesoura.')
        print('Pedra, ', end='')
        sleep(1)
        print('Papel, ', end='')
        sleep(1)
        print('Tesoura!')
        sleep(1)
        print('-=' * 22)
        if opção == 3 and pc == 1:
            print('Você perdeu! O computador escolheu pedra.')
        elif opção == 3 and pc == 2:
            print('Você ganhou! O computador escolheu papel.')
        if opção == 3 and pc == 3:
            print('Empate! Ambos escolheram tesoura.')
            print('-=' * 22)
