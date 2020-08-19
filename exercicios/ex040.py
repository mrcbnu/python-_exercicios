###########################################
#              EXERCICIO 040              #
###########################################
'''CRIE UM PROGRAMA QUE LEIA 2 NOTAS DE UM
ALUNO E CALCULE SUA MEDIA, MOSTRANDO UMA
MENSAGEM NO FINAL DE ACORDO COM A MEDIA
ATINGIDA:
- MEDIA ABAIXO DE 5.0 - REPROVADO;
- MEDIA ENTRE 5.0 E 6.9 - RECUPERAÇÃO;
- MEDIA SUPERIOR A 7.0 - APROVADO.
'''
import time
from datetime import date
data = date.today()
print('\033[1;30m=\033[m' * 58)
print('', '\033[7;1;32m ' * 13, 'F A C U L D A D E  A L V E S', ' \033[7;1;32m' * 12, '\033[m')
print('\033[1;30m=\033[m' * 58)
print('\033[1;30mLANÇAMENTO DE NOTAS',' ' * 27, '{}\033[m\n'.format(data))
nome = str(input('NOME DO ALUNO...:')).upper()
n1 = float(input('PRIMEIRA NOTA...:'))
n2 = float(input('SEGUNDA NOTA....:'))
media = (n1 + n2)/2
print('\n\033[1;30mCALCULANDO A MEDIA . . .\n\n')
time.sleep(2)
if media < 5:
    print('\033[1;30m{}\033[m, sua média foi \033[1;30m{:.2f}\033[m, você foi \033[1;7;30m REPROVADO \033[m'.format(nome,media))
elif media < 7:
    print('\033[1;30m{}\033[m, sua média foi \033[1;30m{:.2f}\033[m, você está em \033[1;7;30m RECUPERAÇÃO \033[m'.format(nome,media))
else:
    print ('\033[1;30m{}\033[m, PARABÉNS, sua media foi \033[1;30m{:.2f}\033[m, você foi \033[1;7;30m APROVADO \033[m'.format (nome,media))
