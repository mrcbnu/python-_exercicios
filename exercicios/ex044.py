###########################################
#              EXERCICIO 044              #
###########################################
'''ELABORE UM PROGRAMA QUE CALCULE O VALOR
A SER PAGO POR UM PRODUTO CONSIDERANDO O SEU
PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:
- A VISTA DINHEIRO/CHEQUE: 10% DESCONTO;
- A VISTA NO CARTÃO: 5% DESCONTO;
- EM 2X NO CARTÃO: PREÇO NORMAL;
- EM 3X NO CARTÃO: 20% JUROS.'''

import time
from datetime import date
data = date.today()
ano = date.today().year
print('\033[1;30m=\033[m' * 58)
print('', '\033[7;1;32m ' * 14, 'M A G A Z I N E   A L V E S', ' \033[7;1;32m' * 12, '\033[m')
print('\033[1;30m=\033[m' * 58)
print('\033[1;30mVENDA DE PRODUTOS',' ' * 24, '{}\033[m\n'.format(data))
preço = float(input('PREÇO DO PRODUTO R$ '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] A VISTA (DINHEIRO/CHEQUE)  - 10% DE DESCONTO
[ 2 ] A VISTA NO CARTÃO  - 5% DE DESCONTO
[ 3 ] 2X NO CARTÃO - PREÇO NORMAL
[ 4 ] 3X NO CARTÃO - 20% DE ACRÉSCIMO''')
opção = int(input('ESCOLHA SUA OPÇÃO...:'))
if opção == 1:
    desc = preço * 10 / 100
    novo = preço - desc
    print('')
    print('\033[1;30mPAGAMENTO A VISTA\033[m')
    print('-' * 30)
    print('VALOR DO PRODUTO: R${:.2f}\n- DESCONTO......: R${:.2f}\nTOTAL...........: \033[1;30mR${:.2f}\033[m'.format(
        preço, desc, novo))
    print('-' * 30)
elif opção == 2:
    desc = preço * 5 / 100
    novo = preço - desc
    print('')
    print('\033[1;30mPAGAMENTO A VISTA NO CARTÃO\033[m')
    print('-' * 30)
    print('VALOR DO PRODUTO: R${:.2f}\n- DESCONTO......: R${:.2f}\nTOTAL...........: \033[1;30mR${:.2f}\033[m'.format(
        preço, desc, novo))
    print('-' * 30)
elif opção == 3:
    desc = preço * 0 / 100
    novo = preço - desc
    print('')
    print('\033[1;30mPAGAMENTO 2x NO CARTÃO\033[m')
    print('-' * 30)
    print('VALOR DO PRODUTO: R${:.2f}\n- DESCONTO......: R${:.2f}\nTOTAL...........: \033[1;30mR${:.2f}\033[m'.format(
        preço, desc, novo))
    print('-' * 30)
elif opção == 4:
    desc = preço * 20 / 100
    novo = preço + desc
    print('')
    print('\033[1;30mPAGAMENTO 3x NO CARTÃO\033[m')
    print('-' * 30)
    print('VALOR DO PRODUTO: R${:.2f}\n+ ACRÉSCIMO.....: R${:.2f}\nTOTAL...........: \033[1;30mR${:.2f}\033[m'.format(
        preço, desc, novo))
    print('-' * 30)
else:
    print('')
    print('\033[1;30mOPÇÃO INVÁLIDA... TENTE NOVAMENTE!\033[m')
