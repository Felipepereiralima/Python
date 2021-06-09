número = int(input('Insira um número inteiro: '))
print('''Escolha uma das operações para calcular:
[ 1 ] Adição
[ 2 ] Multiplicação
[ 3 ] Subtração
[ 4 ] Divisão''')
opção = int(input('Qual operação? '))
número2 = int(input('Insira o segundo número inteiro: '))
if opção == 1:
    soma = int(número) + int(número2)
    print('{} somado com {} é igual a {}.'.format(número,número2, soma))
elif opção == 2:
    multiplicação = número * número2
    print('{} multiplicado por {} é igual a {}.'.format(número, número2, multiplicação))
elif opção == 3:
    subtração = número - número2
    print('{} subtraído por {} é igual a {}.'.format(número, número2, subtração))
elif opção == 4:
    divisão = número / número2
    print('{} dividido por {} é igual a {:.0f}.'.format(número, número2, divisão))
else:
    print('Operação inválida, selecione de 1 a 4, tente novamente.')
