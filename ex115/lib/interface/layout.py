from lib.interface.cores import c
from lib.interface.valida import leiaInt


def linha(s, x=60, cor=0):
    print(f'{c(cor)}{s}'*x, f'{c(0)}')


def cabecalho(x, msg):
    linha(x, cor=9)
    print('{}{}{}'.format(c(11), msg.center(60), c(0)))
    linha(x, cor=9)


def menu(lst):
    cabecalho('-', 'MENU PRINCIPAL')
    op = 1
    for val in lst:
        print(f'{c(7)}[{op}] {val}{c(0)}')
        op += 1
    linha('-', cor=9)
    resp = leiaInt(f'{c(1)}Escolha sua opção{c(0)} ')

    return resp
