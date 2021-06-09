#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros
print('='*10 + ' Atacadão Lima ' + '='*10)
preço = float(input('Digite o valor do produto: R$ '))
print('''Tipos de prazo:
[ 1 ] À vista no dinheiro/cheque: 10% de desconto
[ 2 ] À vista no cartão: 5% de desconto
[ 3 ] Em até 2x no cartão: preço normal
[ 4 ] 3x ou mais no cartão: 20% de juros''')
prazo = int(input('Selecione o prazo de 1 a 4: '))
if prazo == 1:
    valor = preço - (preço * 10)/100
    print('O valor tem desconto de 10% e ficou em R$ {:.2f}.'.format(valor))
elif prazo == 2:
    valor = preço - (preço * 5)/100
    print('O valor tem desconto de 5% e ficou em R$ {:.2f}.'.format(valor))
elif prazo == 3:
    print('O valor de cada parcela fica em R$ {:.2f} e o valor total é de R$ {:.2f}.'.format((preço/2), preço))
elif prazo == 4:
    valor = preço + (preço * 20)/100
    parcela = int(input('Quantas parcelas? '))
    print('O valor de cada parcela fica em R$ {:.2f} ficando no valor total de R$ {:.2f}.'.format((valor/parcela), valor))
else:
    print('Opção inválida, digite de 1 a 4, tente novamente.')
