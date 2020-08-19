###########################################
#              EXERCICIO 106              #
###########################################
"""
Faça um mini-sistema que utilize o Interactive
Help do Python. O usuário vai digitar o comando
e o manual vai aparecer. Quando o usuário digitar
a palavra 'FIM', o programa se encerrará.
Importante: use cores.
"""

from time import sleep

# TABELA DE CORES #
c = (
    '\033[m',        # 0 - sem cor
    '\033[1;30m',    # 1 - branco
    '\033[1;7;30m',  # 2 - branco_in
    '\033[1;31m',    # 3 - vermelho
    '\033[1;30;41m', # 4 - vermelho_in
    '\033[1;32m',    # 5 - verde
    '\033[1;7;32m',  # 6 - verde_in
    '\033[1;33m',    # 7 - amarelo
    '\033[1;7;33m',  # 8 - amarelo_in
    '\033[1;34m',    # 9 - azul
    '\033[1;35m',    # 10 - roxo
    '\033[1;36m',    # 11 - azulc
    '\033[1;7;36m',  # 12 - azul_in
    '\033[1;37m',    # 13 - cinza
    )


def ajuda(x):
    titulo(f'Acessando o manual do comando \'{x}\'', 12)
    print(c[2], end='')
    help(x)
    print(c[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print(f'~' * tam)
    print(f'  {msg}')
    print(f'~' * tam)
    print(c[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 6)
    com = str(input(f'Função ou Biblioteca > '))
    if com.upper() == 'FIM':
        break
    ajuda(com)
titulo('ATÉ LOGO', 4)




