###########################################
#              EXERCICIO 088              #
###########################################
'''Faça um programa que ajude um jogador da
MEGA SENA a criar palpites.O programa vai
perguntar quantos jogos serão gerados e vai
sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''

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
print('{}{:^50}{}'.format(branco_in, 'MEGA SENA', fimdacor))
print()
jogos = []
temp = []
cont = 0
resp = int(input(f'{branco}QUANTOS PALPITES VOCÊ QUER EU FAÇA? {fimdacor}'))
for c in range(resp):
    while True:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
            cont += 1
        if cont >= 6:
            break
    temp.sort()
    jogos.append(temp[:])
    temp.clear()
    cont = 0
    sleep(0.5)
    print(f'{c + 1:2}º PALPITE É {amarelo}{jogos[c]}{fimdacor}')
print()
print('{}{:^50}{}'.format(amarelo_in, 'BOA SORTE !', fimdacor))



