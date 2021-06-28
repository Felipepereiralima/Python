#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma = 0
média = 0
maioridadehomen = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}a Pessoa -----'.format(p))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo M/F? ')).strip()
    soma = soma + idade
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 +1
média = soma / 4
print('A média de idade do grupo é de {} anos.'.format(média))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomen, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
