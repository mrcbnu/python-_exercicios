###########################################
#              EXERCICIO 086              #
###########################################
'''Crie um programa que declare uma matriz
de dimensão 3x3 e preencha com valores lidos
 pelo teclado. No final, mostre a matriz na tela,
  com a formatação correta.'''
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

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'DIGITE O VALOR DE {[linha, coluna]} '))
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^6}]', end=' ')
    print()


