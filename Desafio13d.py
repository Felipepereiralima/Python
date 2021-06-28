#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
número = int(input('Digite um número: '))
vezes = int(input('Quantas vezes? '))
print('='*15)
for c in range (0, vezes):
    tabuada = número * c
    print(número, ' X ', c, ' = ', tabuada)
print('='*15)