###########################################
#              EXERCICIO 058              #
###########################################
'''MELHORE O EX028, ONDE O COMPUTADOR VAI PENSAR
EM UM NUMERO ENTRE 0 E 5. SÓ QUE AGORA O JOGADOR
VAI TENTAR ADIVINHAR ATÉ ACERTAR. MOSTRANDO NO
FINAL QUANTOS PALPITES FORAM NECESSARIOS'''

from random import randint
from time import sleep
num = randint(0,10)
print(num)
erroumais = '\033[1;30mV O C Ê  E R R O U . . .\033[m O NUMERO QUE PENSEI É \033[1;30mM E N O R\033[m'
erroumenos = '\033[1;30mV O C Ê  E R R O U . . .\033[m O NUMERO QUE PENSEI É \033[1;30mM A I O R\033[m'
venceu = '\033[1;30mV O C Ê  A D I V I N H O U . . .\033[m'
parabens = '\033[1;30mPARABÉNS . . .\033[m   '
final = '\033[1;30mFINALMENTE . . .\033[m '
tenta = '\033[1;30mVOCÊ ACERTOU NA {}ª TENTATIVA\033[m'
cont = 0
chute = int(input('Tente adivinhar qual numero de 0 a 10 o computador pensou...: '))
print('P R O C E S S A N D O . . . . \n')
sleep(0.25)
if chute == num:
    cont += 1
    print('*' * len(venceu))
    print(venceu)
    print('*' * len(venceu),'\n')
    print('*' * len(parabens) + '*' * len(tenta))
    print(parabens,end='')
else:
    while chute != num:
        cont += 1
        if chute > num:
            print('*' * len(erroumais))
            print(erroumais)
            print('*' * len(erroumais), '\n')
            print(erroumais)
        elif chute < num:
            print('*' * len(erroumenos))
            print(erroumenos)
            print('*' * len(erroumenos), '\n')
        chute = int(input('Digite seu novo palpite '))
    print('*' * len(final) + '*' * len(tenta))
    print(final, end='')
print(tenta.format(cont))
print('*' * len(final) + '*' * len(tenta))
