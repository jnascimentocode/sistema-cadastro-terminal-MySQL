import mysql.connector
from time import sleep
from rich.table import Table
from rich.console import Console

try:
    db = mysql.connector.connect(host='localhost', user='root', password='', database='cadastrocli')
    cursor = db.cursor()
    if db.is_connected():
        print('\033[32m Conectado ao banco de dados... \033[m')
except:
    print(' - Não foi possivel acessar o banco de dados - ')
    exit('APLICAÇÃO NÃO INICIALIZADA')

def inserirDados(nome, nascimento, sexo, nacionalidade):

    sql = 'INSERT INTO clientes (nome, nascimento, sexo, nacionalidade) VALUES (%s, %s, %s, %s)'
    valores = (nome, nascimento, sexo, nacionalidade)
    cursor.execute(sql, valores)
    db.commit()
    print('\033[32m CLIENTE CADASTRADO COM SUCESSO! \033[m')
    sleep(0.5)

def visualizarDados():

    console = Console()
    table = Table(title='LISTA DE CLIENTES')
    table.add_column('ID', justify='center')
    table.add_column('NOME', justify='center')
    table.add_column('NASCIMENTO', justify='center')
    table.add_column('SEXO', justify='center')
    table.add_column('NACIONALIDADE', justify='center')

    sql = 'SELECT * FROM clientes '

    cursor.execute(sql)
    linhas = cursor.fetchall()

    print(' - Acessando registros na tabela...')
    sleep(1)
    print('')

    for linha in linhas:
        data = str(linha[2])

        table.add_row(str(linha[0]), str(linha[1]), data, str(linha[3]), str(linha[4]))

    console.print(table)
    print(' - \033[32m Total de Registros encontrados: \033[m', cursor.rowcount)
    sleep(1)

def validacaoDB(id):

    sql = f'SELECT id FROM clientes where id ={id}'
    cursor.execute(sql)
    resultado = cursor.fetchone()
    if resultado is None:
        print(f'\033[0;31m USUARIO {id} NÃO EXISTE \033[m')
    else:
        return id


def alterarDados(id, opção, nome='', nascimento='', sexo='', nacionalidade=''):

    while True:

        sql = f'SELECT id FROM clientes where id ={id}'
        cursor.execute(sql)
        resultado = cursor.fetchone()
        if resultado is None:
            print(f'\033[0;31m USUARIO {id} NÃO EXISTE \033[m')
            sleep(1)
            break

        while True:
            resposta = str(input(f'DESEJA ALTERAR OS DADOS DO USUARIO {id} ? [S/N]: ')).strip().upper()
            if resposta in 'SN':
                break
            else:
                print('\033[0;31m VALOR INVÁLIDO! DIGITE APENAS S OU N \033[m')

        if resposta in 'Nn':
            print('OPÇÃO CANCELADA')
            sleep(1)
            break
        else:
            if opção == 1:
                sql = f'UPDATE clientes SET nome = "{nome}"  WHERE id = {id}'
                cursor.execute(sql)
            elif opção == 2:
                sql = f'UPDATE clientes SET nascimento = "{nascimento}"  WHERE id = {id}'
                cursor.execute(sql)
            elif opção == 3:
                sql = f'UPDATE clientes SET sexo = "{sexo}"  WHERE id = {id}'
                cursor.execute(sql)
            elif opção == 4:
                sql = f'UPDATE clientes SET nacionalidade = "{nacionalidade}"  WHERE id = {id}'
                cursor.execute(sql)
            db.commit()
            sleep(2)
            return print(f'\033[32m DADOS DO REGISTRO {id} ALTERADOS COM SUCESSO!\033[m')
            break

def excluirDados(id):

    while True:

        sql = f'SELECT id FROM clientes where id ={id}'
        cursor.execute(sql)
        resultado = cursor.fetchone()
        if resultado is None:
            print(f'\033[0;31m USUARIO {id} NÃO EXISTE \033[m')
            sleep(1)
            break

        while True:
            resposta = str(input(f'DESEJA DELETAR O USUARIO {id} ? [S/N]: ')).strip().upper()
            if resposta in 'SN':
                break
            else:
                print('\033[0;31m VALOR INVÁLIDO! DIGITE APENAS S OU N \033[m')

        if resposta in 'Ss':
            sql = f'DELETE FROM clientes WHERE id = {id}'
            cursor.execute(sql)
            db.commit()
            return print(f'\033[32m DADOS DO REGISTRO {id} EXCLUÍDOS COM SUCESSO!\033[m')
            sleep(2)
        else:
            print('OPERAÇÃO CANCELADA')
            sleep(2)
            break













