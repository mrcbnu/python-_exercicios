###########################################
#              EXERCICIO 076              #
###########################################
'''Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de
preços, organizando os dados em forma tabular.'''

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

produtos = ['Lapis', 2,'Caderno', 15, 'Caneta', 3, 'Borracha', 4, 'Pincel', 6,
            'Grampeador', 20, 'Clips', 15, 'Calculadora', 45, 'Régua', 9, 'Lapiseira', 25]
print('-' * 40)
print('{:^40}'.format('TABELA DE PREÇOS'))
print('-' * 40)
for c in produtos:
    if type(c) == str:
        print(f'{c:.<30}', end=' ')
    else:
        print(f'R${c:>7.2f}')
print('-' * 40)