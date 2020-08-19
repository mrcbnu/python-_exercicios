###########################################
#              EXERCICIO 099              #
###########################################
'''
Faça um programa que tenha uma função chamada
maior(), que receba vários parâmetros com
valores inteiros. Seu programa tem que analisar
todos os valores e dizer qual deles é o maior.
'''
from time import sleep

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


def maior(* val):
    print('-' * 40)
    print('ANALIZANDO OS VALORES PASSADOS....')
    cont = maior = 0
    for num in val:
        print(f'{num}', end=' ')
        if cont == 0:
            maior = num
        elif num > maior:
            maior = num
        cont += 1
    print(f'formam informados {len(val)} valores ao todo')
    print(f'O MAIOR VALOR INFORMADO FOI {maior}')
    sleep(2)


# programa principal
maior(1, 6, 8, 4, 2, 5, 6)
maior(2, 6, 8, 10, 0)
maior(0, 90, 1, 5)


