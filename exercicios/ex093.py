###########################################
#              EXERCICIO 093              #
###########################################
'''
Crie um programa que gerencie o aproveitamento
de um jogador de futebol. O programa vai ler o
nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em
cada partida. No final, tudo isso será guardado
em um dicionário, incluindo o total de gols feitos
durante o campeonato.'''

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

jogador = dict()
gols = []

print('{}{:^80}{}'.format(amarelo_in, 'CAMPEONATO BRASILEIRO', fimdacor))
print('{}{:^80}{}'.format(azulc_in, 'APROVEITAMENTO DO JOGADOR', fimdacor))
print()

jogador['nome'] = str(input(f'{branco} NOME DO JOGADOR: {fimdacor}')).upper()
jogador['partidas'] = int(input(f'{amarelo} QUANTAS PARTIDAS DISPUTADAS: {fimdacor}'))
print()
for j in range(jogador['partidas']):
    gols.append(int(input(f' QUANTOS GOLS MARCADOS NA {j +1}ª PARTIDA? ')))

jogador['gols'] = gols[:]      # chave 'gols' recebe lista gols
jogador['total'] = sum(gols)   # chave 'total recebe a soma de todos os itens da lista gols usando a função sum

print()
print('{}{:^80}{}'.format(branco_in, 'ANALIZANDO . . . ', fimdacor))
sleep(1)
print()
print(jogador)
print('_' * 80)
sleep(1)

for k, v in jogador.items():
    print(f' O campo {branco}{k}{fimdacor} tem o valor {branco}{v}{fimdacor} ')
print('_' * 80)
sleep(1)
print()
print(f' O JOGADOR {amarelo}{jogador["nome"]}{fimdacor} JOGOU {branco}{jogador["partidas"]}{fimdacor} PARTIDAS E:')
for i, v in enumerate(jogador['gols']):
    print(f'   => Marcou {branco}{v}{fimdacor} gols na {branco}{i +1}ª{fimdacor} partida')
print(f' TOTAL DE {branco}{jogador["total"]}{fimdacor} GOLS MARCADOS!')
print('_' * 80)


