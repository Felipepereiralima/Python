#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
Distancia = float(input('Qual a distância da sua viagem? '))
if Distancia <= 200:
    Preço = Distancia*0.50
    print('A viagem custará R${:.2f} para {}Km.'.format(Preço, Distancia))
else:
    Preço = Distancia*0.45
    print('A viagem custará R${:.2f} para {}Km.'.format(Preço, Distancia))
