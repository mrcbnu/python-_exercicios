###########################################
#              EXERCICIO 043              #
###########################################
'''DESENVOLVA UM PROGRAMA QUE LEIA O PESO
E ALTURA DE UMA PESSOA, CALCULE SEU IMC E
MOSTRE SEU STATUS DE ACORDO COM A TABELA ABAIXO:
- ABAIXO DE 18,5: ABAIXO DO PESO;
- ENTRE 18,5 E 25: PESO IDEAL;
- 25 A 30: SOBREPESO;
- 30 A 40: OBESIDADE;
- ACIMA DE 40: OBESIDADE MORBIDA'''

import time
from datetime import date
data = date.today()
ano = date.today().year
print('\033[1;30m=\033[m' * 58)
print('', '\033[7;1;32m ' * 9, 'C A C U L A D O R A   D E   I M C ', ' \033[7;1;32m' * 10, '\033[m')
print('\033[1;30m=\033[m' * 58)
print('\033[1;30mDIGITE SEUS DADOS',' ' * 29, '{}\033[m\n'.format(data))
nome = str(input('NOME.......:')).upper()
peso = float(input('PESO.....:'))
altura= float(input('ALTURA..:'))
imc = peso / (altura ** 2)
print('\n\033[1;30mAGUARDE! CALCULANDO SEU IMC...\033[m\n')
time.sleep(1)
print('\033[1;30m{}\033[m seu IMC é \033[1;30m{:.2f}\033[m,'.format(nome,imc),end='')
if imc < 18.5:
    print(' você está \033[1;30mABAIXO DO PESO\033[m ideal!')
elif imc < 25:
    print(' você está no \033[1;30mPESO\033[m ideal!')
elif imc < 30:
    print(' você está com \033[1;30mSOBREPESO\033[m!')
elif imc < 40:
    print(' você está \033[1;30mOBESO\033[m!')
else:
    print(' você está com \033[1;30mOBESIDADE MÓRBIDA\033[m!')
