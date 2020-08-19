###########################################
#              EXERCICIO 028              #
###########################################
'''ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR
PENSAR UM NUMERO INTEIRO ENTRE 0 E 5 E PEÇA
PARA O USUARIO TENTAR DESCOBRIR QUAL FOI O
NUMERO ESCOLHIDO PELO COMPUTADOR. O PROGRAMA
DEVERÁ ESCREVER NA TELA SO O USUARIO VENCEU
OU PERDEU'''

from random import randint
from time import sleep
cont = 0
num = randint(1,5)
print(num)
chute = int(input('Tente adivinhar qual numero de 0 a 5 o computador pensou...: '))
print('P R O C E S S A N D O . . . .')
sleep(3)
print()
if chute == num:
    cont += 1
    print('*' * 37)
    print('P A R A B É N S  V O C Ê  V E N C E U')
    print ('*' * 37)
else:
    while chute != num:
        print ('*' * 37)
        print ('V O C Ê  E R R O U . . . T E N T E  A D I V I N H A R  N O V A M E N T E!')
        print ('*' * 37, '\n')
        chute = int (input ('Digite seu novo palpite'))
        cont += 1
    print ('P A R A B É N S  V O C Ê  V E N C E U')
print ('VOCÊ ACERTOU NA {}ª TENTATIVA'.format (cont))
