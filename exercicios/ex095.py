###########################################
#              EXERCICIO 095              #
###########################################
'''
Aprimore o desafio 93 para que ele funcione
com vários jogadores, incluindo um sistema
de visualização de detalhes do aproveitamento
de cada jogador.
'''


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

time = list()
jogador = dict()
gols = list()

print('{}{:^80}{}'.format(amarelo_in, 'PEREBA´S FUTBOOL CLUB', fimdacor))
print('{}{:^80}{}'.format(azulc_in, 'APROVEITAMENTO DOS JOGADORES', fimdacor))
print()
# ---------------------- entrada de dados -------------------------#
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input(f'{branco} JOGADOR: {fimdacor}')).upper()
    partidas = int(input(f'{branco} PARTIDAS: {fimdacor}'))
    for j in range(partidas):
        gols.append(int(input(f'{branco} GOLS MARCADOS NA {j +1}ª PARTIDA? {fimdacor}')))
    jogador['gols'] = gols[:]      # chave 'gols' recebe lista gols
    jogador['total'] = sum(gols)   # chave 'total recebe a soma de todos os itens da lista gols usando a função sum
    time.append(jogador.copy())

    while True:
        opção = str(input(f'{amarelo} DESEJA CADASTRAR OUTRO JOGADOR [S/N] {fimdacor}')).upper()[0]
        if opção in 'SN':
            break
        print(f'{vermelho} OPÇÃO INVÁLIDA... {fimdacor}')

    if opção == 'N':
        break
    print('_' * 80)
print()
print('{}{:^80}{}'.format(branco_in, 'ANALIZANDO . . . ', fimdacor))
sleep(1)
print()
# ----------------- apresentação geral do cadastro -----------------#
print('-' * 50)
print(f'{"| COD":<6}{"| NOME":<15}{"| GOLS":<20}{"| TOTAL":<6}')
for k, v in enumerate(time):
    print(f'| {k+1:<4}| {v["nome"]:<13}| {str(v["gols"]):<18}| {v["total"]:<5}')
print()
print('-' * 50)
# -------------- apresentação indivudual do jogador -----------------#
while True:
    cod = int(input(f'{branco} MOSTRAR DADOS DE QUAL JOGADOR? {fimdacor}(999 para sair)  '))
    print('-' * 50)
    if cod == 999:
        break
    if len(time) >= cod > 0:
        print(f'{branco} LEVANTAMENTO DO JOGADOR {time[cod-1]["nome"]}{fimdacor}')
        for i, v in enumerate(time[cod-1]['gols']):
            print(f'   => Marcou {branco}{v}{fimdacor} gols na {branco}{i + 1}ª{fimdacor} partida')
        print('-' * 50)
    if cod > len(time) or cod == 0:
        print(f'{vermelho} NÃO EXISTE JOGADOR COM ESSE CODIGO... TENTE NOVAMENTE{fimdacor}')

print()
print(time)
