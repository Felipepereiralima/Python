from random import randint
Pergunta = 'Não'
Pergunta = str(input('Gostaria de jogar o dado Sim/Não? ')).strip().upper()
while Pergunta in 'Sim sim s':
    Pergunta = str(input('Gostaria de jogar o dado Sim/Não? '))
    if Pergunta in 'Sim sim':
        Numero = int(randint(1, 6))
        print('Seu número do dado é {}.'.format(Numero))
    else:
        print('Que pena, fica pra próxima.')
