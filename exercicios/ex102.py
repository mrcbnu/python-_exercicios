###########################################
#              EXERCICIO 102              #
###########################################
"""
Crie um programa que tenha uma função fatorial()
que receba dois parâmetros: o primeiro que indique
o número a calcular e outro chamado show, que
será um valor lógico (opcional) indicando se
será mostrado ou não na tela o processo de cálculo
do fatorial.
"""
from time import sleep

from random import randint

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


def fatorial(num, show=False):
    """
    FUNÇÃO QUE CALCULA FATORIAL DE UM NUMERO
    :param num: numero a ser calculado
    :param show: (opcional) Mostra ou não a conta
    :return: O valor do fatorial de num
    """
    print(f'{num}! = ', end='')
    fat = 1
    for cont in range(num, 0, -1):
        if show:
            print(cont, end='')
            if cont > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= cont
    return fat


# programa principal
opc = ' '
show = 0
num = int(input(f'{branco}Digite um numero para calcular o seu Fatorial {fimdacor}'))
while opc not in 'SN':
    opc = str(input(f'{amarelo}Você quer ver que exiba a conta inteira [S/N] {fimdacor} ')).upper()[0]
if opc == 'S':
    show = 1
print(fatorial(num, show))
