###########################################
#              EXERCICIO 093              #
###########################################
'''Crie um programa que leia nome, sexo e idade
de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários
em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

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

tot_cad = soma_id = 0
pessoa = dict()        # dicionário
cadastro = list()      # lista

# --------------------------  ENTRADA DE DADOS --------------------------------- #
opção = ' '
while opção not in 'N':
    print('-' * 30)
    pessoa['nome'] = str(input(f'{branco}NOME.........: {fimdacor}')).upper()
    while True:
        pessoa['sexo'] = str(input(f'{branco}SEXO [M/F]...: {fimdacor}')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print(f'{vermelho}OPÇÃO INVÁLIDA!{fimdacor}')
    pessoa['idade'] = int(input(f'{branco}IDADE........: {fimdacor}'))
    soma_id += pessoa['idade']
    tot_cad += 1
    cadastro.append(pessoa.copy())
    pessoa.clear()
    print()
    while True:
        opção = str(input(f'{amarelo}DESEJA CONTINUAR [S/N] {fimdacor}')).upper()
        if opção in 'NS':
            break
        print(f'{vermelho}OPÇÃO INVALIDA...')
    print()

# ------------------------ ANALISE DOS DADOS ----------------------------- #
media = soma_id / len(cadastro)
print('{}{:^80}{}'.format(amarelo_in, 'RESULTADOS',fimdacor))
print()
print(f'{branco}A) FORAM CADASTRADAS {len(cadastro)} PESSOAS{fimdacor}')
print(f'{branco}B) A MEDIA DE IDADE É DE {media:5.2f} ANOS{fimdacor}')
print(f'{branco}C) AS MULHERES CADASTRADAS FORAM{fimdacor}', end=' | ')
for c in cadastro:
    if c['sexo'] in 'F':
        print(f'{amarelo}{c["nome"]}{fimdacor}', end=' | ')
print(f'\n{branco}D) PESSOAS COM IDADE ACIMA DA MEDIA:{fimdacor}')
for c in cadastro:
    if c['idade'] >= media:
        print(f'{amarelo}   {c["nome"]} COM {c["idade"]} ANOS DE IDADE{fimdacor}')
print()
print('{}{:^80}{}'.format(amarelo_in, 'ENCERRADO', fimdacor))
