###########################################
#              EXERCICIO 085              #
###########################################
'''Crie um programa onde o usuário possa digitar
sete valores numéricos e cadastre-os em uma lista
única que mantenha separados os valores pares e
ímpares. No final, mostre os valores pares e
ímpares em ordem crescente.'''

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

lista = [[], []]
temp = 0

for c in range(7):
    temp = int(input(f'DIGITE {c+1}º NUMERO...: '))
    if temp % 2 == 0:
        lista[0].append(temp)
    else:
        lista[1].append(temp)
lista[0].sort()
lista[1].sort()
print('\n{}{:^50}{}'.format(amarelo_in, 'RESULTADO', fimdacor))
print(f'OS NUMEROS PARES DIGITADOS FORAM : {lista[0]}')
print(f'OS NUMEROS IMPARES DIGITADOS FORAM :{lista[1]}')
