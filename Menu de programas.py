#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
primeiro = int(input('Digite um valor: '))
segundo = int(input('Digite o segundo valor: '))
escolha = 0
while escolha != 5:
    print('-=-'*10)
    print('''Você quer:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    escolha = int(input('Qual a sua escolha? '))
    if escolha == 1:
        soma = primeiro + segundo
        print('A soma entre {} e {} é {}.'.format(primeiro, segundo, soma))
    elif escolha == 2:
        multiplica = primeiro * segundo
        print('A multiplicação entre {} e {} é {}.'.format(primeiro, segundo, multiplica))
    elif escolha == 3:
        if primeiro > segundo:
            print('O número {} é maior que o número {}.'.format(primeiro, segundo))
        elif primeiro == segundo:
            print('Os números {} e {} são iguais.'.format(primeiro, segundo))
        elif primeiro < segundo:
            print('O número {} é maior que o número {}.'.format(segundo, primeiro))
    elif escolha == 4:
        primeiro = int(input('Digite um novo número: '))
        segundo = int(input('Digite um outro novo número: '))
    elif escolha == 5:
        print('Fechando o programa...')
        sleep(1)
    else:
        print('Opção inválida, digite de 1 a 5.')
print('Obrigado por usar nosso programa.')
