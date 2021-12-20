from interface import *
from conexao import *
from datetime import datetime
from time import sleep

while True:
    cabecalho('MENU PRINCIPAL')

    opção = menu(['CADASTRAR CLIENTE', 'VISUALIZAR CLIENTE',
                  'ALTERAR DADOS CLIENTE', 'EXCLUIR CLIENTE',
                  'SAIR DO SISTEMA'])

    if opção == 1:

        cabecalho('CADASTRO DO CLIENTE')
        nome = str(input('NOME: '))

        while True:
            try:
                ano = str(input('DATA NASCIMENTO: '))
                nascimento = datetime.strptime(ano, '%d/%m/%Y').date()
                break
            except:
                print('DIGITAR NO FORMATO [DD/MM/AA]')

        while True:
            sexo = str(input('SEXO [M/F]: ')).strip().upper()
            if sexo not in 'MmFf':
                print('FAVOR DIGITAR FORMATO VÁLIDO.')
            else:
                break

        nacionalidade = str(input('NACIONALIDADE: '))

        inserirDados(nome, nascimento, sexo, nacionalidade)

    elif opção == 2:

        cabecalho('ACESSO AOS DADOS')
        visualizarDados()

    elif opção == 3:

        while True:
            cabecalho('ALTERAR DADOS CLIENTE')

            id = validacao_dado('DIGITE O NUMERO DO REGISTRO QUE SERÁ ALTERADO: ')

            if validacaoDB(id) is None:
                sleep(1)
                break

            print('QUAL DADO VOCÊ GOSTARIA DE ALTERAR?')

            opção = menu(['NOME', 'NASCIMENTO',
                          'SEXO', 'NACIONALIDADE'])

            if opção == 1:
                nome = str(input('NOME: '))
                alterarDados(id, opção, nome=nome)
                break
            elif opção == 2:

                while True:
                    try:
                        ano = str(input('DATA NASCIMENTO: '))
                        nascimento = datetime.strptime(ano, '%d/%m/%Y').date()
                        break
                    except:
                        print('DIGITAR NO FORMATO [DD/MM/AA]')
                alterarDados(id, opção, nascimento=nascimento)
                break
            elif opção == 3:

                while True:
                    sexo = str(input('SEXO [M/F]: ')).strip().upper()
                    if sexo not in 'MmFf':
                        print('FAVOR DIGITAR FORMATO VÁLIDO.')
                    else:
                        break
                alterarDados(id, opção, sexo=sexo)
                break
            elif opção == 4:

                nacionalidade = str(input('NACIONALIDADE: '))
                alterarDados(id, opção, nacionalidade=nacionalidade)
                break

    elif opção == 4:

        cabecalho('EXCLUIR CLIENTE')

        id = validacao_dado('DIGITE O NUMERO DO REGISTRO QUE SERÁ DELETADO: ')
        excluirDados(id)

    elif opção == 5:

        while True:
            while True:
                resposta = str(input('DESEJA SAIR DO SISTEMA? [S/N]: ')).strip().upper()
                if resposta in 'SN':
                    break
                else:
                    print('\033[0;31m VALOR INVÁLIDO! DIGITE APENAS S OU N \033[m')

            if resposta in 'Nn':
                print('\033[0;31m OPÇÃO CANCELADA \033[m')
                sleep(1)
                break
            else:
                print('...SAINDO DO SISTEMA...')
                sleep(1)
                print('\033[1;30;44m <<< VOLTE SEMPRE! >>> \033[m')
                exit()

    else:
        print('\033[0;31m DIGITE UMA OPÇÃO VÁLIDA. \033[m')
        sleep(0.5)
