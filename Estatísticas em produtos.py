s = c = m = cont = 0
barato = ' '
print('='*50)
print('{:^50}'.format('LOJA DESCONTAÇO'))
print('='*50)
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: R$'))
    cont += 1
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    s += preço
    if preço > 1000:
        c += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    if pergunta == 'N':
        break
print('{:-^50}'.format(' FIM DA COMPRA '))
print(f'O total gasto na compra foi de R${s:.2f}.')
print(f'Temos {c} produtos que custam mais de R$1.000.')
print(f'O produto mais barato é {barato} que custa {menor:.2f}.')
