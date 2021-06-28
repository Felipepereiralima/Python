#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range (1, 7):
    número = int(input('Digite um número: '))
    if número % 2 == 0:
        soma = soma + número
        cont = cont + 1
print('Você informou {} números pares e a soma foi {}.'.format(cont, soma))