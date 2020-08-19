def aumentar(val=0, taxa=0):
    '''
    -> Função que aumenta o valor conforme a taxa informada
    :param val: valor base do claculo
    :param taxa: porcentagem do aumento
    :return: retorna o valor com aumento
    '''
    tot = val + (val * taxa / 100)
    return tot


def diminuir(val=0, taxa=0):
    tot = val - (val * taxa / 100)
    return tot


def dobro(val=0):
    tot = val * 2
    return tot


def metade(val=0):
    tot = val / 2
    return tot


def moeda(val=0, moeda='R$'):
    return f'{moeda} {val:.2f}'.replace('.', ',')
