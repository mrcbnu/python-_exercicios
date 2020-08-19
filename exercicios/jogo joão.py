from sty import fg, rs
from time import sleep
from random import randint
# TABELA DE CORES #
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
print(fg.blue +'OLÁ' )
print(f'{amarelo}-{fimdacor}' * 80)
print('{}{:^80}{}'.format(amarelo_in,'J O G O  D A  M A T E M Á T I C A',fimdacor))
print(f'{amarelo}-{fimdacor}' * 80,'\n')
print(f'{branco}OLÁ AMIGUINHO, TUDO BEM? VAMOS BRINCAR DE FAZER CONTAS?{fimdacor}')
nome = str(input(f'{branco}QUAL O SEU NOME?{fimdacor} ')).upper()
print(f'{amarelo}{nome}, VOCÊ ESTÁ FAZENDO AS ATIVIDADES DA ESCOLA? {fimdacor}')
sleep(2)
print(f'{verde}ESPERO QUE SIM, ENTÃO VAMOS VER SE VOCÊ ESTÁ BEM DE MATEMÁTICA?{fimdacor}')
sleep(2)
print(f'{vermelho}EU VOU TE DAR 10 CONTINHAS DE MAIS E MENOS PRA VOCÊ RESPONDER...{fimdacor}')
sleep(2)
print(f'{azulc}ESTÁ PREPARADO?{fimdacor}')
sleep(2)
print(f'{azulc}VAMOS LÁ?{fimdacor}\n')
placar = 0
while True:
    print('{}{:^80}{}'.format(branco_in,'F A S E  1 - A D I Ç Ã O',fimdacor))
    for c in range(0,5):
        num = [randint(1,50), randint(1,50)]
        total = num[0] + num [1]
        resp = int(input(f'{branco}{num[0]} + {num[1]} = {fimdacor} '))
        sleep(0.5)
        if resp == total:
            print(f'{amarelo}PARABENS {nome}... VOCÊ ACERTOU!{fimdacor}')
            placar += 1
        else:
            print(f'{vermelho}QUE PENA! O CERTO É {total} ...  NÃO DESISTA, VOCÊ VAI CONSEGUIR!{fimdacor}')
    print('{}{:^80}{}'.format(branco_in, 'F A S E  2 - S U B T R A Ç Ã O', fimdacor))
    for c in range(0,5):
        num = [randint(10, 40), randint(1,10)]
        total = num[0] - num[1]
        resp = int(input(f'{branco}{num[0]} - {num[1]} = {fimdacor} '))
        sleep(0.5)
        if resp == total:
            print(f'{amarelo}PARABENS {nome}... VOCÊ ACERTOU!{fimdacor}')
            placar += 1
        else:
            print(f'{vermelho}QUE PENA! O CERTO É {total} ...  NÃO DESISTA, VOCÊ VAI CONSEGUIR!{fimdacor}')
    print('\n{}{:^80}{}'.format(vermelho_in,'R E S U L T A D O ',fimdacor))
    if placar > 7:
        print(f'\n{branco}MUITO BEM {nome} ! VOCÊ ACERTOU {placar} CONTAS...{fimdacor}')
    else:

        print(f'\n{branco}AI AI AI {nome} !, VOCÊ PRECISA TREINAR MAIS! ACERTOU APENAS {placar}{fimdacor}\n')
    break
print(f'\n{branco}GAME OVER . . .  ATÉ A PRÓXIMA!{fimdacor}')
