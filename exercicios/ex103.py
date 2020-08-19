###########################################
#              EXERCICIO 103              #
###########################################
"""
Faça um programa que tenha uma função chamada
ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha
do jogador, mesmo que algum dado não tenha sido
informado corretamente.
"""


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


def ficha(jog, gols):
    print(f'{branco}O jogador {jog} fez {gols} gols{fimdacor}')


nome = str(input('Qual o nome do jogador...: ')).upper()
gol = str(input('Quantos gols ele fez.....: '))
if nome.strip() == '':
    nome = '<desconhecido>'
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

ficha(nome, gol)