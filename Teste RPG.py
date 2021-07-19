from time import sleep
from random import randint
print('=' * 110)
print('Averum é um mundo que foi devastado pela Grande Guerra Celestial que consumiu a maior parte da mana existente.')
print('=' * 110)
sleep(0)
print('Você é um guerreiro, porém perdeu a sua espada vá encontre algo para se defender.')
sleep(0)
pergunta0 = str(input('Deseja explorar o mapa [SIM/NÃO]? ')).strip().upper()[0]
sleep(0)
if pergunta0 == 'S':
    print('Demora muito, mas você chega em uma cidade destruída pela guerra e decide vasculhar uma loja de armas.')
    sleep(0)
    pergunta1 = str(input('Você encontra uma espada, deseja pegá-la [SIM/NÃO]? ')).strip().upper()[0]
    sleep(0)
    if pergunta1 == 'S':
        print('Agora com a espada você sente mais confiante e seguro e decide explorar mais.')
        sleep(0)
        pergunta2 = str(input('Você vê uma caverna quer entrar [SIM/NÃO]? ')).strip().upper()[0]
        sleep(0)
        if pergunta2 == 'S':
            print('Você entra na caverna e de repente...')
            sleep(0)
            saudeMonstro = 5
            saudePlayer = 10
            #FAZER COM O WHILE OU COM O FOR
            while True:
                pergunta3 = str(input('Você encontra um ogro com um tesouro deseja abatê-lo [SIM/NÃO]? ')).strip().upper()[0]
                sleep(0)
                numeroDado = randint(1, 6)
                numeroDado2 = randint(1, 6)
                #O ATAQUE DO PLAYER
                if pergunta3 == 'S' and numeroDado == 1 or numeroDado == 2:
                    print('O seu ataque errou!')
                elif pergunta3 == 'S' and numeroDado == 3 or numeroDado == 4:
                    print('O seu ataque acertou! Tirou 1 de dano.')
                    saudeMonstro -= 1
                elif pergunta3 == 'S' and numeroDado == 5 or numeroDado == 6:
                    print('O seu ataque acertou! Tirou 2 de dano.')
                    saudeMonstro -= 2
                #O ATAQUE DO OGRO
                if pergunta3 == 'S' and numeroDado2 == 1 or numeroDado2 == 2:
                    print('O ataque do ogro errou!')
                elif pergunta3 == 'S' and numeroDado2 == 3 or numeroDado2 == 4:
                    print('O ataque do ogro acertou! Tirou 1 de dano.')
                    saudePlayer -= 1
                elif pergunta3 == 'S' and numeroDado2 == 5 or numeroDado2 == 6:
                    print('O ogro acertou! Tirou 2 de dano.')
                    saudePlayer -= 2
                else:
                    print('Você deixa o ogro pra lá e continua sua jornada para encontrar alimento.')
                    break
                # CONTINUAR DAQUI...
        else:
            print('Você prossegue adiante pois tem medo de cavernas.')
            #PROSSEGUIR AQUI...
    else:
        print('Você está sem nenhuma arma e é atacado por um grupo de orcs e acaba morrendo, GAME OVER!')
else:
    print('Você está sem nenhuma arma e é atacado por uma matilha de lobos e acaba morrendo, GAME OVER!')
