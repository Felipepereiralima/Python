from random import randint
while True:
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Gostaria de jogar o dado Sim/Não? ')).strip().upper()[0]
    if pergunta == 'S':
        número = randint(1, 6)
        print(f'Seu número do dado é {número}.')
    if pergunta == 'N':
        print('Obrigado por usar o programa dado.')
        break
