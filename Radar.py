#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
v = int(input('Digite sua velocidade: '))
if v <= 80:
    print('Você está na velocidade correta.')
else:
    m = (v-80)*7.00
    print('Você foi multado em R${:.2f}!'.format(m))
