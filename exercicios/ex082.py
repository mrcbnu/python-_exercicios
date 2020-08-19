###########################################
#              EXERCICIO 082              #
###########################################
'''Crie um programa que vai ler vários números
e colocar em uma lista. Depois disso, crie duas
listas extras que vão conter apenas os valores
pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

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

lista = []
par = []
impar = []
while True:
    num = int(input('DIGITE UM NUMERO...: '))
    lista.append(num)
    if num % 2 ==0:
        par.append(num)
    else:
        impar.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('DESEJA CONTINUAR [S/N]')).upper().strip()
    if resp == 'N':
        break
print(lista)
print(par)
print(impar)
