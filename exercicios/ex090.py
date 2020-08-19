###########################################
#              EXERCICIO 090              #
###########################################
''' Faça um programa que leia nome e média
de um aluno, guardando também a situação em
um dicionário. No final, mostre o conteúdo
da estrutura na tela.'''

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

aluno = {}
print('{}{:^50}{}'.format(verde_in, 'RESULTADO FINAL', fimdacor))
print()
aluno['nome'] = str(input(f'{branco}NOME....: {fimdacor}')).upper()
aluno['media'] = float(input(f'{branco}MEDIA FINAL....: {fimdacor}'))
print(f'{branco}SITUAÇÃO....: {fimdacor}', end='')
sleep(1)
if aluno['media'] < 7:
    aluno['situação'] = 'REPROVADO'
    print(f'{vermelho_in} {aluno["situação"]} {fimdacor}')
else:
    aluno['situação'] = 'APROVADO'
    print(f'{azulc_in} {aluno["situação"]} {fimdacor}')
print()
print(f'{branco}{aluno}{fimdacor}')