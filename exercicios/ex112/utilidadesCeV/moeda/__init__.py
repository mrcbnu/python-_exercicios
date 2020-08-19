def aumentar(val=0, taxa=0, form=False):
    '''
    -> Função que aumenta o valor conforme a taxa informada
    :param val: valor base do claculo
    :param taxa: porcentagem do aumento
    :return: retorna o valor com aumento
    '''
    tot = val + (val * taxa / 100)
    if form:
        return moeda(tot)
    else:
        return tot


def diminuir(val=0, taxa=0, form=False):
    tot = val - (val * taxa / 100)
    if form:
        return moeda(tot)
    else:
        return tot


def dobro(val=0, form=False):
    tot = val * 2
    if form:
        return moeda(tot)
    else:
        return tot


def metade(val=0, form=False):
    tot = val / 2
    if form:
        return moeda(tot)
    else:
        return tot


def moeda(val=0, moeda='R$'):
    return f'{moeda} {val:.2f}'.replace('.', ',')


def resumo(val=0, txa=5, txd=10):
    print('-' * 30)
    print('{:^30}'.format('RESUMO DO VALOR'))
    print('-' * 30)
    print(f'{c(1)}', end='')
    print(f'Preço analizado: {moeda(val):>13}')
    print(f'Dobro do preço: {dobro(val, True):>14}')
    print(f'Metade do preço: {metade(val, True):>13}')
    print(f'{txa}% de aumento: {aumentar(val, txa, True):>15}')
    print(f'{txd}% de redução: {diminuir(val, txd, True):>14}')
    print('-' * 30)
