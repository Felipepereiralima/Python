#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
numero = randint(0, 10)
chute = 1
palpite = int(input('Digite um número: '))
while numero != palpite:
    if palpite != numero:
        chute = chute + 1
    palpite = int(input('Digite outro número: '))
print('Acertou, foram {} tentativas!'.format(chute))
print('Fim de jogo!')
