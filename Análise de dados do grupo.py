#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

i = h = m = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite um sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        i += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m += 1
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja cadastrar mais uma pessoa Sim/Não? ')).strip().upper()[0]
    if pergunta == 'N':
        break
print(f'São {i} pessoas maiores de idade.\nForam cadastrados {h} homens.\nE {m} mulheres tem menos de 20 anos.')
