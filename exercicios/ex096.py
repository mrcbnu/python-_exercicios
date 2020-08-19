###########################################
#              EXERCICIO 096              #
###########################################
'''
Faça um programa que tenha uma função chamada
área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a
área do terreno.
'''

from time import sleep
from datetime import date
from random import randint
from operator import itemgetter

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


def área(l, c):
    total = l * c
    print(f'{amarelo}A ÁREAL TOTAL É DE {branco}{total} {amarelo}m2{fimdacor}')


# programa principal #
print(f'{branco}-{fimdacor}' * 30)
print(f'{amarelo}CALCULO DE AREA DO TERRENO{fimdacor}')
print()
lar = float(input(f'{branco}DIGITE A LARGURA.......: '))
com = float(input(f'{branco}DIGITE O COMPRIMENTO...: '))
área(lar, com)
