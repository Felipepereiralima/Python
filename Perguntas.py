perguntas = ['DEVO SAIR DE CASA HOJE?', 'QUANTOS ANOS EU TENHO?', 'ATOM OU SUBLIME TEXT?']
respostas = ['NÃO', 'EU SEI LA PORRA', 'ATOM']
perguntaFeita = str(input('Pergunta: ')).upper()
for x in range(0, 3):
    if perguntaFeita == perguntas[x]:
        print (respostas[x])