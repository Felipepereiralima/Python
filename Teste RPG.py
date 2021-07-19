from time import sleep
from random import randint
print('=' * 110)
print('Averum é um mundo que foi devastado pela Grande Guerra Celestial que consumiu a maior parte da mana existente.')
print('=' * 110)
sleep(2)
print('Você é um guerreiro, porém perdeu a sua espada vá encontre algo para se defender.')
sleep(2)
pergunta0 = str(input('Deseja explorar o mapa [S/N]? ')).strip().upper()[0]
sleep(2)
if pergunta0 == 'S':
    print('Demora muito, mas você chega em uma cidade destruída pela guerra e decide vasculhar uma loja de armas.')
    sleep(2)
    pergunta1 = str(input('Você encontra uma espada, deseja pegá-la [S/N]? ')).strip().upper()[0]
    sleep(2)
    if pergunta1 == 'S':
        print('Agora com a espada você sente mais confiante e seguro e decide explorar mais.')
        sleep(2)
        pergunta2 = str(input('Você vê uma caverna quer entrar [S/N]? ')).strip().upper()[0]
        sleep(2)
        if pergunta2 == 'S':
            print('Você entra na caverna e de repente...')
            sleep(2)
            saudeMonstro = 5
            saudePlayer = 5
            pergunta3 = str(input('Você encontra um ogro com um tesouro deseja abatê-lo [S/N]? ')).strip().upper()[0]
            if pergunta3 == 'S':
                saudeMonstro = 4
                saudePlayer = 4
                while True:
                    numeroDado = randint(1, 6)
                    if numeroDado == 1:
                        sleep(2)
                        print('Você errou o ataque!')
                    if numeroDado == 2:
                        sleep(2)
                        print('O ogro errou o ataque.')
                    if numeroDado == 3:
                        sleep(2)
                        print('Você acertou o ataque! Deu 1 de dano.')
                        saudeMonstro = saudeMonstro - 1
                    if numeroDado == 4:
                        sleep(2)
                        print('O ogro acertou o ataque! Deu 1 de dano.')
                        saudePlayer = saudePlayer - 1
                    if numeroDado == 5:
                        sleep(2)
                        print('Você acertou um ataque crítico!! Deu 2 de dano.')
                        saudeMonstro = saudeMonstro - 2
                    if numeroDado == 6:
                        sleep(2)
                        print('O ogro acertou um ataque crítico!! Deu 2 de dano.')
                        saudePlayer = saudePlayer - 2
                    if saudeMonstro <= 0:
                        sleep(2)
                        print('Parabéns você matou o ogro! Ganhou o tesouro!')
                        sleep(2)
                        print('Você pega todo o tesouro e caminha todo feliz.')
                        sleep(2)
                        print('Você vê um mercador que oferece uma armadura em troca do tesouro.')
                        sleep(2)
                        pergunta6 = str(input('Deseja trocar o tesouro pela armadura [S/N]? ')).strip().upper()[0]
                        sleep(2)
                        if pergunta6 == 'S':
                            print('Você ganhou 4 pontos de proteção.')
                            saudePlayer = saudePlayer + 4
                        else:
                            print('A troca não é feita, mas depois você fica se lamentando por não ter trocado.')
                        #PODE CONTINUAR DAQUI
                        break
                    if saudePlayer <= 0:
                        sleep(2)
                        print('GAME OVER, você morreu para o ogro!')
                        break
                #AQUI É O RETORNO DO LOOP DO WHILE TRUE
            else:
                print('Você deixa o ogro pra lá e continua sua jornada para encontrar alimento.')
                sleep(2)
                print('Logo se depara com uma senhora, de uns 80 anos, ela lhe oferece uma maçã.')
                pergunta4 = str(input('Pegar a maça [S/N]? ')).strip().upper()[0]
                sleep(2)
                if pergunta4 in 'S':
                    print('Você comeu a maçã e morreu envenenado, GAME OVER!')
                else:
                    print('Você sabiamente recusa presente de estranhos.')
                    #CONTINUAR DAQUI
        else:
            print('Você prossegue adiante pois tem medo de cavernas...')
            sleep(2)
            print('Logo adiante existe um rio, você observa a correnteza...')
            sleep(2)
            pergunta5 = str(input('Você quer atravessar o rio [S/N]? ')).strip().upper()[0]
            if pergunta5 == 'S':
                print('Você atravessa tranquilamente para o outro lado.')
                #CONTINUAR DAQUI
            else:
                print('Um grupo de bandidos roubam a sua espada e te matam, GAME OVER!')
    else:
        print('Você está sem nenhuma arma e é atacado por um grupo de orcs e acaba morrendo, GAME OVER!')
else:
    print('Você está sem nenhuma arma e é atacado por uma matilha de lobos e acaba morrendo, GAME OVER!')