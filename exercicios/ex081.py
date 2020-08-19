###########################################
#              EXERCICIO 080              #
###########################################
'''
Crie um programa que vai ler vários números e colocar
em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
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

lista = []
while True:
    lista.append(int(input(f'{branco}DIGITE UM NUMERO {fimdacor}')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input(f'{amarelo}DESEJA CONTINUAR [S/N] {fimdacor}')).upper().strip()
    if resp == 'N':
        break
lista.sort(reverse=True)
print('\n{}{:^50}{}'.format(amarelo_in,'RESULTADOS', fimdacor))
if len(lista) == 1:
    print(f'\n{azulc}FOI DIGITADO APENAS {len(lista)} NUMERO')
else:
    print(f'\n{azulc}FORAM DIGITADOS {len (lista)} NUMEROS')
if 5 in lista:
    print(f'\n{verde}O NUMERO 5 ESTA NA LISTA')
else:
    print(f'\n{vermelho}O NUMERO 5 NÃO ESTÁ NA LISTA')
print(f'\n{roxo}LISTA EM ORDEM DECRESCENTE: {branco}{lista}{fimdacor}{fimdacor}\n')
print('\n{}{:^50}{}'.format(amarelo_in,'F I M', fimdacor))

