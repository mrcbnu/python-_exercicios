
def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip().replace(' ', '')
        if entrada.isalpha():
            print(f'ERRO: \"{entrada}\" não é um preço válido!')
        elif entrada.strip() == '':
            print(f'ERRO: \"{entrada}\" não é um preço válido!')
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):
    """
    ->> função que valida a digitação de um numero inteiro.
    :var ok:     é o flag,por padrão o valor inicial é 'False', a validação somente
                 estará concluida quando o valor de ok for 'True'.
    :var num:    é a variavel que recebe a entrada de valor digitado pelo usuário
    :var val:  é a variavel que vai receber o valor inteiro válido.
    :param msg:  é a mensagem solicitando ao usuario que digite um numero.
    :return:     retorna o numero válido.
    """
    ok = False
    while not ok:
        val = str(input(msg)).replace(',', '.').strip().replace(' ', '')
        if val.isnumeric():
            ok = True
            return float(val)
        else:
            print(f'ERRO: \"{entrada}\" não é um numero inteiro válido!')
