x = input('Digite um numero ')
dicionario_numerico = {
    'unidade':{
        'um':1,
        'dois':2,
        'três' : 3,
        'quatro':4,
        'cinco':5,
        'seis':6,
        'sete':7,
        'oito':8,
        'nove':9,
        'dez':10
    },
    'onzeAodezenove':{
        'onze':11,
        'doze':12,
        'treze':13,
        'quatorze':14,
        'quinze':15,
        'dezeseis':16,
        'dezesete':17,
        'dezoito':18,
        'dezenove':19,

    },
    'vinteanoventa':{
        'vinte':20,
        'trinta':30,
        'quarenta':40,
        'cinquenta':50,
        'sessenta':60,
        'setenta':70,
        'oitenta':80,
        'noventa':90,

    },
    'cemAteNoventaenove':{

        'cento':100,
        'duzentos':200,
        'trezentos':300,
        'quatrocentos':400,
        'quinhentos':500,
        'seiscentos':600,
        'setecentos':700,
        'oitocentos':800,
        'novecentos':900,


    },

}

digitos = x
if x.isnumeric():
    x = len(x)


def UnidadeDezena():

    if x == 1:#-verifica se o usuario digitou um unico numero
        for k, v in dicionario_numerico['unidade'].items():
            if int(digitos) == v:
                print('-' * 10)
                print(k)
                print('-' * 10)

    if x == 2 and digitos[0] == '1' and digitos[1] == '0':
        print('-' * 10)
        print(list(dicionario_numerico['unidade'])[9])
        print('-' * 10)

    if x == 2 and digitos[0] == '1':
        for k, v in dicionario_numerico['onzeAodezenove'].items():
            valor = str(v)
            if digitos[1] == valor[1]:
                print('-' * 10)
                print(k)
                print('-' * 10)



    if x == 2 and digitos[0] != '1':
        for k, v in dicionario_numerico['vinteanoventa'].items():
            valor = str(v)
            if digitos[0] == valor[0]:
                saveK = k
                for k, v in dicionario_numerico['unidade'].items():
                    if digitos[1] == str(v):
                        print('-' * 10)
                        print(saveK, 'e', k)
                        print('-' * 10)

    if x == 2 and digitos[1] == '0':
        for k, v in dicionario_numerico['vinteanoventa'].items():
            valor = str(v)
            if digitos[0] == valor[0]:
                print('-' * 10)
                print(k)
                print('-' * 10)
def centenas():
    centena = ''
    dezena = ''
    unidade = ''
    if x == 3 and digitos[1] != '0' and digitos[2] != '0':
        for k, v in dicionario_numerico['cemAteNoventaenove'].items():
            valor = str(v)
            if digitos[0] == valor[0]:
                centena = k


        if (int(digitos[1])) > 0 and (int(digitos[1])) < 2:
            for k1, v1 in dicionario_numerico['onzeAodezenove'].items():
                valor = str(v1)
                if digitos[1] == valor[0] and digitos[2] == valor[1]:
                    dezena = k1

        else:
            for k1, v1 in dicionario_numerico['vinteanoventa'].items():
                valor = str(v1)
                if digitos[1] == valor[0]:
                    dezena = k1

            for k2, v2 in dicionario_numerico['unidade'].items():
                valor = str(v2)
                if digitos[2] == valor:
                    unidade = k2
        print('-'*10)
        print(centena, 'e', dezena, unidade)
        print('-'*10)

    elif x == 3 and digitos[1] == '0' and digitos[2] == '0':
        for k, v in dicionario_numerico['cemAteNoventaenove'].items():
            valor = str(v)
            if digitos[0] == valor[0]:
                print('-' * 10)
                print(k)
                print('-' * 10)
    elif x == 3 and digitos[1] != '0' and digitos[2] == '0':
        for k, v in dicionario_numerico['cemAteNoventaenove'].items():
            valor = str(v)
            if digitos[0] == valor[0]:
                centena = k
        for k1, v1 in dicionario_numerico['vinteanoventa'].items():
            valor = str(v1)
            if digitos[1] == valor[0]:
                dezena = k1
        print('-' * 10)
        print(centena, 'e', dezena)
        print('-' * 10)
    elif x == 3 and digitos[1] == '0' and digitos[2] != '0':
        for k, v in dicionario_numerico['cemAteNoventaenove'].items():
            valor = str(v)
            if digitos[0] == valor[0]:
                centena = k
        for k2, v2 in dicionario_numerico['unidade'].items():
            valor = str(v2)
            if digitos[2] == valor:
                unidade = k2
        print('-' * 10)
        print(centena, 'e', unidade)
        print('-' * 10)



while x != 1000:
    UnidadeDezena()
    centenas()

    x = input('Digite um numero ')

    digitos = x
    if x.isnumeric():
        x = len(x)