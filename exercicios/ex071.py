###########################################
#              EXERCICIO 071              #
###########################################
'''CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO
DE UM CAIXA ELETRONICO. NO INCIO PERGUNTE AO
USUARIO QUAL SERÁ O VALOR A SER SACADO E O
PROGRAMA VAI INFORMAR QUANTAS CEDULAS DE CADA
VALOR SAERÃO ENTREGUES.
OBS: CONSIDERE QUE O CAIXA POSSUI CEDULAS DE
R$50, R$20, R$10 E R$1'''

print('-' * 50)
print('\033[1;30m{:^50}\033[m'.format('B A N C O  A L V E S'))
print('-' * 50)
print('\033[1;30m{:^50}\033[m'.format(' S A Q U E'))
valor = int(input('VALOR DO SAQUE: R$ '))
total = valor
ced = 50
contced = 0
totalced = 0
print('-' * 50)
print('\033[1;30mCONFIRA SEU DINHEIRO\033[m\n')
while True:
    if total >= ced:
        total -= ced
        contced += 1
    else:
        if contced > 0:
            totalced = ced * contced
            print(f'TOTAL DE {contced} CEDULA(S) DE {ced} = R${totalced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        contced = 0
        if total ==0:
            break
print('')
print('\033[1;30mOBRIGADO PELA PREFERENCIA... VOLTE SEMPRE')
