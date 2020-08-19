###########################################
#              EXERCICIO 098              #
###########################################
'''
Faça um programa que tenha uma função chamada
contador(), que receba três parâmetros: início,
fim e passo. Seu programa tem que realizar três
contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
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

# FUNÇÕES #
def contador(i, f, p):
    print(f'{amarelo}CONTAGEM DE {i} A {f} DE {p} EM {p} {fimdacor}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{branco}{cont}', end=' ')
            sleep(.25)
            cont += p
        print(f'FIM {fimdacor}')
    else:
        cont = i
        while cont >= f:
            print(f'{branco}{cont}', end=' ')
            sleep(.25)
            cont -= p
        print(f'FIM {fimdacor}')


# PROGRAMA PRINCIPAL #
contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
print(f'{vermelho}AGORA VOCE DEFINE COMO SERÁ A CONTAGEM{fimdacor}')
ini = int(input('INICIO..:'))
fim = int(input('FIM.....:'))
pas = int(input('PASSO...:'))
contador(ini, fim, pas)
