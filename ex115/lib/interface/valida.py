from ex115.lib.interface.cores import c


def leiaInt(msg):
    '''
    -> Função que valida a entrada de um numero inteiro
    :param msg: indicação ao usuario informando a entrada do valor a ser validado
    :return: retorna o valor correto
    '''
    while True:
        try:
            num = int(input(msg))
        except (TypeError, ValueError):
            print('não é um numero inteiro valido!')
            continue
        except KeyboardInterrupt:
            print(f'{c(5)}O usuário preferiu não informar o valor {c(0)}')
            return 0
        else:
            return num


def leiaFloat(msg):
    '''
    -> Função que valida a entrada de um numero real
    :param msg: indicação ao usuario informando a entrada do valor a ser validado
    :return: retorna o valor correto
    '''
    while True:
        try:
            num = float(input(msg))
        except (TypeError, ValueError):
            print('não é um numero real valido!')
            continue
        else:
            return num
