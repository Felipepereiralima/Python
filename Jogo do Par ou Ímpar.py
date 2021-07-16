#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
v = 0
while True:
    n = int(input('Digite um número: '))
    nm = randint(1, 100)
    soma = nm + n
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar [P/I]? ')).strip().upper()[0]
    print(f'Você jogou {n} e a máquina jogou {nm}. Total de {soma}.', end=' ')
    print('Deu Par.' if soma % 2 == 0 else 'Deu Ímpar.')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você Venceu!')
            v = v + 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você Venceu!')
            v = v + 1
        else:
            print('Você Perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'O jogo acabou! Você venceu {v} vezes.')
