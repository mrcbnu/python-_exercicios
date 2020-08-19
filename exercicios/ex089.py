###########################################
#              EXERCICIO 089              #
###########################################
''' Crie um programa que leia nome e duas notas
de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de
cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.'''

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

aluno = []
while True:
    nome = str(input('NOME.....: ')).upper()
    av1 = float(input('NOTA 1...: '))
    av2 = float(input('NOTA 2...: '))
    media = (av1 + av2) / 2
    aluno.append([nome, [av1, av2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('DESEJA CONTINUAR O CADASTRO [S/N]')).upper()
    if resp == 'N':
        break
print('\n{}{:^50}{}'.format(branco_in, 'LISTA DE ALUNOS', fimdacor))
print()
print(f'{"| Cod":<6} {"| NOME":<30} {"| MEDIA":<6}')

for i, v in enumerate(aluno):
    print(f'|{i + 1:^6}| {v[0]:<29}|{v[2]:^6}')
print()
print(f'{branco}PARA CONSULTAR AS NOTAS DOS ALUNOS INDIVIDUALMENTE DIGITE O CODIGO, 0 PARA SAIR...:{fimdacor}')
while True:
    cod = int(input('CODIGO DO ALUNO...:'))
    if cod == 0:
        break
    if cod <= len(aluno):
        print()
        print('{}{:^50}{}'.format(azulc_in,'BOLETIM',fimdacor))
        print()
        print(f'{"| ALUNO":<15}{"| NOTAS"}')
        print(f'|{branco} {aluno[cod-1][0]:<13}{fimdacor}|{branco}{aluno[cod-1][1]}{fimdacor}')


