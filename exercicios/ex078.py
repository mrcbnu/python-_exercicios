###########################################
#              EXERCICIO 078              #
###########################################
'''Faça um programa que leia 5 valores numéricos
e guarde-os em uma lista. No final, mostre qual
foi o maior e o menor valor digitado e as suas
respectivas posições na lista. '''

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

num = []
for c in range(0, 5):
    num.append(int(input(f'DIGITE O NUMER DA POSIÇÃO {c} DA LISTA.: ')))
menor = min(num)
maior = max(num)
print('-' * 50)
print(f'VOCÊ DIGITOU OS NUMEROS {num}')
print(f'O MENOR NUMERO DA LISTA É {menor} NA(s) POSICÃO(ões)... ', end='')
for pos, val in enumerate(num):
    if val == menor:
            print(f'{pos} ... ', end='')
print(f'\nO MAIOR NUMERO DA LISTA É {maior} NA(s) POSIÇÃO(ões)... ', end='')
for pos, val in enumerate(num):
        if val == maior:
            print(f'{pos} ... ', end='')
