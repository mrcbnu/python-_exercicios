###########################################
#              EXERCICIO 052              #
###########################################
'''FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO
E DIGA SE ELE É OU NÃO UM NUMERO PRIMO'''
import time
n = int(input('DIGITE UM NUMERO E VEJA SE É PRIMO...:'))
cont = 0
for c in range(1,n+1):
    if n % c == 0:
        print('\033[1;30m',c,end='')
        time.sleep(0.1)
        cont += 1
    else:
        print('\033[1;34m',c,end='')
        time.sleep(0.1)
if cont == 2:
    print('\nO número \033[1;30m{}\033[m foi dividido \033[1;30m{}\033[m vezes,é um número \033[1;4;30mPRIMO\033[m'.format(n,cont))
else:
    print ('''\nO número \033[1;30m{}\033[m foi dividido \033[1;30m{}\033[m vezes, \033[1;4;30mNÃO É PRIMO\033[m'''.format (n, cont))
