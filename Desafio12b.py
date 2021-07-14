#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
número = int(input('Insira um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para Binário é igual a {}'.format(número, bin(número)[2:]))
elif opção == 2:
    print('{} convertido para Octal é igual a {}'.format(número, oct(número)[2:]))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(número, hex(número)[2:]))
else:
    print('Opção inválida, tente novamente.')