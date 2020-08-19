from lib.interface.layout import *


def arqExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print('Houve um Erro na criação do arquivo!')
    else:
        print(f'Arquivo {arquivo} criado com sucesso!')


def leiaArquivo(arquivo):
    try:
        a = open(arquivo, 'r')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabecalho('-', 'PESSOAS CADASTRADAS')
        linha('-', 44)
        print('| {}|{}|'.format('NOME'.center(30), 'IDADE'.center(10)))
        linha('-', 44)
        for v in a:
            dado = v.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'| {dado[0]:<30}|{dado[1]:^10}|')
        linha('-', 44)
    finally:
        a.close()


def entraDados(arquivo):
    try:
        a = open(arquivo,'at')
    except:
        print('Ops! problemas em abrir arquivo')
    else:
        cabecalho('+', 'CADASTRO DE PESSOAS')
        nome = str(input('Nome: ')).upper()
        idade = leiaInt('Idade: ')
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Ops! problemas ao gravar os dados!')
        else:
            print(f'Registro de {nome} cadastrado com sucesso!')
            a.close()

