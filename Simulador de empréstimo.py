#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
Casa = float(input('Valor da casa: R$ '))
Salário = float(input('Seu salário: R$ '))
Anos = int(input('Em quantos anos você vai pagar? '))
Cálculo = Casa / (Anos*12)
Salário2 = Salário*30/100
if Cálculo < Salário2:
    print('O empréstimo foi aprovado com parcelas de {:.2f}.'.format(Cálculo))
else:
    print('O empréstimo foi negado pois o valor da parcela R${:.2f} superou os 30% do salário R${:.2f}.'.format(Cálculo, Salário2))
print('Obrigado por usar nosso app!')
