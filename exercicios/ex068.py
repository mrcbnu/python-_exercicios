###########################################
#              EXERCICIO 067              #
###########################################
'''FAÇA UM PROGRAMA QUE JOGUE PAR OU IMPAR
COM O COMPUTADOR. O JOGO SERÁ INTERROMPIDO
QUANDO O JOGADOR PERDER, MOSTRANDO O TOTAL
DE VITORIAS CONSECUTIVAS QUE ELE CONQUISTOU
NO FINAL DO JOGO'''

from random import randint
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
print(f'{branco}-=' * 25, f'{fimdacor}')
print('{}{:^50}{}'.format(azulc,'VAMOS BRINCAR DE PAR OU ÍMPAR',fimdacor))
print(f'{branco}-=' * 25, f'{fimdacor}')
vitoria = 0
while True:
    cpu = randint(0,10)
    chute = int(input(f'{roxo}DIGA UM NUMERO ENTRE 0 E 10: {fimdacor}'))
    parouimpar = str(input(f'{vermelho}PAR OU IMPAR [P/I]? {fimdacor}')).upper()[0].strip()
    while parouimpar not in 'PI':
        parouimpar = str(input(f'{vermelho}PAR OU IMPAR [P/I]? {fimdacor}')).upper()[0].strip()
    soma = cpu + chute
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print(f'O COMPUTADOR ESCOLHEU{branco} {cpu}{fimdacor} e VOCÊ ESCOLHEU {branco}{chute} {fimdacor}= {branco}{soma}{fimdacor}')
    print('{}{:^50}{}'.format(azulc_in,resultado,fimdacor))
    if resultado == 'PAR' and parouimpar == 'P' or resultado == 'IMPAR' and parouimpar == 'I':
        print('{}{:^50}{}'.format(amarelo_in,' V O C Ê  V E N C E U  ! ! !',fimdacor))
        print(f'{branco}-=' * 25, f'{fimdacor}')
        print('{}{:^50}{}'.format(azulc, 'VAMOS JOGAR NOVAMENTE', fimdacor))
        print(f'{branco}-=' * 25, f'{fimdacor}')
        vitoria += 1
    else:
        print('{}{:^50}{}'.format(vermelho_in,' V O C Ê  P E R D E U  ! ! !',fimdacor))
        print('-' * 50)
        break
print('{}{:^50}{}'.format(verde_in,'G A M E  O V E R  ! ! !',fimdacor))
print('{}{:^50}{}'.format(branco_in,vitoria,fimdacor))
print('{}{:^50}{}'.format(verde_in,'VITÓRIAS',fimdacor))

