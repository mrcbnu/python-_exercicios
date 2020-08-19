###########################################
#              EXERCICIO 080              #
###########################################
'''Crie um programa onde o usuário possa digitar
cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.  '''

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

lista = []
for cont in range(0,5):
    num = int(input('digite um numero '))
    if cont == 0 or num > lista[-1]:
        lista.append(num)
        print('ADICIONADO NO FINAL DA LISTA')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'ADICIONADO NA POSIÇÃO {pos} DA LISTA')
                break
            pos += 1
print(lista)


