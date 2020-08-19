###########################################
#              EXERCICIO 045              #
###########################################
'''CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR
JOGAR JOTEMPO COM VOCÊ: PEDRA, PAPEL, TESOURA'''

from time import sleep
from random import randint
#for opção == 3:
itens = ('PEDRA','PAPEL','TESOURA')
comp = randint(0,2)
print('\033[1;30m=\033[m' * 58)
print('', '\033[7;1;32m ' * 20, 'J O K E M P O', ' \033[7;1;32m' * 20, '\033[m')
print('\033[1;30m=\033[m' * 58)
print('')
print('''ESCOLHA SUA OPÇÃO:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\n''')
opção = int(input('QUAL A SUA JOGADA?'))
print('JO ',end='')
sleep(1)
print('KEM ',end='')
sleep(1)
print('KO ')
sleep(1)
print('* ' * 25)
print('VOCÊ ESCOLHEU \033[1;30m{}\033[m'.format(itens[opção]))
print('COMPUTADOR ESCOLHEU \033[1;30m{}\033[m'.format(itens[comp]))
if opção == 0:
    sleep(1)
    if comp == 0:
        print('\n\033[1;7;30m EMPATE \033[m')
    if comp == 1:
        print ('\n\033[1;7;30m COMPUTADOR VENCEU \033[m')
    else:
        print ('\n\033[1;7;30m VOCÊ VENCEU \033[m')
elif opção == 1:
    sleep (1)
    if comp == 0:
        print ('\n\033[1;7;30m VOCÊ VENCEU \033[m')
    if comp == 1:
        print ('\n\033[1;7;30m EMPATE \033[m')
    else:
        print ('\n\033[1;7;30m COMPUTADOR VENCEU \033[m')
elif opção == 2:
    sleep (1)
    if comp == 0:
        print ('\n\033[1;7;30m COMPUTADOR VENCEU \033[m')
    if comp == 1:
        print ('\n\033[1;7;30m VOCÊ VENCEU \033[m')
    else:
        print ('\n\033[1;7;30m EMPATE \033[m')
else:
    print('OPÇÂO INVALIDA.... TENTE NOVAMENTE')