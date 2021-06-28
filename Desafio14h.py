#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
número = cont = soma = 0
número = int(input('Digite um número [999 pra parar]: '))
while número != 999:
    cont = cont + 1
    soma = soma + número
    número = int(input('Digite um número [999 pra parar]: '))
print('Você digitou {} números e a soma entre eles foi de {}.'.format(cont, soma))
