#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
pergunta = str('Ss')
cont = 0
média = 0
soma = 0
maior = 0
menor = 0
while pergunta not in 'Nn':
    número = int(input('Digite um número: '))
    pergunta = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    soma = soma + número
    cont = cont + 1
    if cont == 1:
        maior = menor = número
    else:
        if número > maior:
            maior = número
        if número < menor:
            menor = número
média = soma/cont
print('Você digitou {} números e a média foi de {}.'.format(cont, média))
print('O maior valor foi de {} e o menor valor foi de {}.'.format(maior, menor))
