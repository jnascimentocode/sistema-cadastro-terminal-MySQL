from time import sleep

def validacao_dado(i):
    while True:
        try:
            n = int(input(i))
        except (ValueError, TypeError):
            print('\033[0;31m VALOR INVÁLIDO. \033[m')
            sleep(0.5)
        else:
            return n

def linha(tam=55):
    return '_' * tam

def cabecalho(txt):
    print(linha())
    print(f'\033[1;30;m{txt.center(55)}\033[m')
    print(linha())

def menu(lista):

    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = validacao_dado('\033[33m DIGITE A OPÇÃO: \033[m ')
    return opc

def tratar_sexo(s):
    while True:
        sexo = s
        if sexo not in 'MmFf':
            print('FAVOR DIGITAR FORMATO VÁLIDO.')
        else:
            return sexo
            break
