###########################################
#              EXERCICIO 074              #
###########################################
'''CRIE UM PROGRAMA QUE VAI GERAR CINCO NUMEROS
ALEATÓRIOS E COLOCAR EM UMA TUPLA. DEPOIS DISSO
MOSTRE A LISTAGEM DE NUMEROS GERADOS E TAMBEM
INDIQUE O MENOR E O MAIOR VALOR QUE ESTA NA TUPLA'''

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

tupla = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))
print(tupla)
maior = menor = tupla[0]
for c in range(0, 5):
    if tupla[c] > maior:
        maior = tupla[c]
    if tupla[c] < menor:
        menor = tupla[c]
print(f'MAIOR = {maior}\nMENOR = {menor}')
# usando a função max e min para mostrar o maior e menor numero da tupla #
print('OS NUMEROS SORTEADOS FORAM ', end='')
for n in tupla:
    print(f'{n}', end=' ')
print(f'\nO MAIOR NUMERO FOI {max(tupla)}')
print(f'O MENOR MUMERO FOI {min(tupla)}')
