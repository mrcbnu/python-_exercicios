###########################################
#              EXERCICIO 091              #
###########################################
''' Crie um programa onde 4 jogadores joguem
um dado e tenham resultados aleatórios. Guarde
esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.'''

from time import sleep
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

print('{}{:^50}{}'.format(verde_in, 'JOGO DE DADOS', fimdacor))
print(f'\n{branco}QUATRO JOGADORES IRÃO JOGAR DADOS, QUEM SERÁ QUE VAI GANHAR?{fimdacor}')

jogo = {}
ranking = []
for j in range(4):
    print(f'\n{branco}O JOGADOR {j + 1} VAI JOGAR O DADO....  ', end='')
    sleep(1)
    dado = randint(1, 6)
    print(f'{amarelo_in} {dado} {fimdacor}')
    jogo[j] = dado
    sleep(1)
sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print()
print('{}{:^50}{}'.format(azulc_in, 'RESULTADO FINAL', fimdacor))
print()
for i, v in enumerate(ranking):
    print(f'\n{amarelo}{i+1}º LUGAR {fimdacor} -> {branco}JOGADOR {v[0] + 1}, '
          f'ACERTOU {amarelo_in} {v[1]} {fimdacor}{branco} PONTOS! {fimdacor}')
print()
print(jogo)
print(ranking)
