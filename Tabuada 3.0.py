#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('='*36)
    for c in range (1, 11):
        tabuada = n * c
        print(f'{n} X {c} = {tabuada}')
    print('=' * 36)
print('Programa tabuada encerrado. Obrigado por usar.')