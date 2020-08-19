###########################################
#              EXERCICIO 084              #
###########################################
'''Faça um programa que leia nome e peso de
várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

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

cadastro = []
temp = []
pesado = leve = 0
while True:
    temp.append(str(input(f'{branco}NOME...:')).upper())
    temp.append(int(input(f'PESO...:{fimdacor}')))
    if len(cadastro) == 0:
        pesado = leve = temp[1]
    else:
        if temp[1] >= pesado:
            pesado = temp[1]
        if temp[1] <= leve:
            leve = temp[1]
    cadastro.append(temp[:])
    temp.clear()
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input(f'{amarelo}DESEJA CONTINUAR [S/N]{fimdacor}')).upper()
    if resp == 'N':
        break
print()
print('{}{:^50}{}'.format(vermelho_in,'RESULTADO',fimdacor))
print(f'\nFORAM CADASTRADOS {len(cadastro)} PESSOAS')
for valor in cadastro:
    if valor[1] == pesado:
        print(f'{amarelo}{valor[0]}{fimdacor},',end=' ')
print(f'TEM O MAIOR PESO COM {verde}{pesado}{fimdacor} KILOS')
for valor in cadastro:
    if valor[1] == leve:
        print(f'{amarelo}{valor[0]}{fimdacor},',end=' ')
print(f'TEM O MENOR PESO COM {verde}{leve}{fimdacor} KILOS')




