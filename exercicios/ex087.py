###########################################
#              EXERCICIO 087              #
###########################################
'''Aprimore o ex086, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
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
pares = soma = maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'DIGITE O VALOR DE {[linha, coluna]} '))
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
        if linha == 1:
            if matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]
        if coluna == 2:
            soma += matriz[linha][coluna]
print()
print('{}{:^50}{}'.format(branco_in, 'RESULTADOS', fimdacor))
print()
print(f'{branco}A MATRIZ 3X3 DIGITADO FICOU ASSIM:{fimdacor}')
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'{amarelo}[{matriz[linha][coluna]:^6}]{fimdacor}', end=' ')
    print()
print()
print(f'{branco}A SOMA DE TODOS OS NUMEROS PARES É : {azulc}{pares}{fimdacor}')
print(f'{branco}A SOMA DOS VALORES DA TERCEIRA COLUNA É : {azulc}{soma}{fimdacor}')
print(f'{branco}O MAIOR VALOR DA SEGUNDA LINHA É : {azulc}{maior}{fimdacor}')