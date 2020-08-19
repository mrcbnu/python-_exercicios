###########################################
#              EXERCICIO 104              #
###########################################
"""
Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante 'a função
input() do Python, só que fazendo a validação
para aceitar apenas um valor numérico.
"""


# TABELA DE CORES #
branco = '\033[1;30m'
branco_in = '\033[1;7;30m'
vermelho = '\033[1;31m'
vermelho_in = '\033[1;7;31m'
verde = '\033[1;32m'
verde_in = '\033[1;7;32m'
amarelo = '\033[1;33m'
amarelo_in = '\033[1;7;33m'
azul = '\033[1;34m'
roxo = '\033[1;35m'
azulc = '\033[1;36m'
azulc_in = '\033[1;7;36m'
cinza = '\033[1;37m'
fimdacor = '\033[m'


def leiaInt(msg):
    """
    ->> função que valida a digitação de um numero inteiro.
    :var ok:     é o flag,por padrão o valor inicial é 'False', a validação somente
                 estará concluida quando o valor de ok for 'True'.
    :var num:    é a variavel que recebe a entrada de valor digitado pelo usuário
    :var valor:  é a variavel que vai receber o valor inteiro válido.
    :param msg:  é a mensagem solicitando ao usuario que digite um numero.
    :return:     retorna o numero válido.
    """
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print(f'{vermelho}ERRO! Digite um numero inteiro válido!{fimdacor}')
        if ok:
            break
    return valor


# PROGRAMA PRINCIPAL
num = leiaInt('Digite um numero inteiro...: ')
print(f'{branco}Você acabou de digitar o número {amarelo}{num}{fimdacor}')

