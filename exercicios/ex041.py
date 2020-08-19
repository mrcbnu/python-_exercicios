###########################################
#              EXERCICIO 040              #
###########################################
'''A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA
DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DO
ATLETA E MOSTRE SUA CATEGORIA DE ACORDO COM A IDADE:
- ATÉ 9 ANOS: MIRIM;
- ATÉ 14 ANOS: INFANTIL;
- ATÉ 19 ANOS: JUNIOR;
- ATÉ 20 ANOS: SENIOR;
- ACIMA : MASTER'''

import time
from datetime import date
data = date.today()
ano = date.today().year
print('\033[1;30m=\033[m' * 58)
print('', '\033[7;1;32m ' * 10, 'CONFEDERAÇÃO NACIONAL DE NATAÇÃO', ' \033[7;1;32m' * 11, '\033[m')
print('\033[1;30m=\033[m' * 58)
print('\033[1;30mCATEGORIAS DOS ATLETAS',' ' * 24, '{}\033[m\n'.format(data))
nome = str(input('NOME DO ATLETA.......:')).upper()
nasc = int(input('ANO DE NASCIMENTO....:'))
idade = ano - nasc
print('\n\033[1;30m{}\033[m, você tem \033[1;30m{}\033[m anos de idade\n'.format(nome,idade))
print('AGUARDE! VERIFICANDO SUA CATEGORIA....\n')
time.sleep(2)
if idade <= 9:
    print('-'*50)
    print('\033[1;30m{} sua categoria é MIRIM\033[m'.format(nome))
    print('-'*50)
elif idade <= 14:
    print ('-' * 50)
    print ('\033[1;30m{} sua categoria é INFANTIL\033[m'.format (nome))
    print ('-' * 50)
elif idade <= 19:
    print ('-' * 50)
    print ('\033[1;30m{} sua categoria é JUNIOR\033[m'.format (nome))
    print ('-' * 50)
elif idade <= 25:
    print ('-' * 50)
    print ('\033[1;30m{} sua categoria é SENIOR\033[m'.format (nome))
    print ('-' * 50)
else:
    print ('-' * 50)
    print ('\033[1;30m{} sua categoria é MASTER\033[m'.format (nome))
    print ('-' * 50)
