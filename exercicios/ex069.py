###########################################
#              EXERCICIO 069              #
###########################################
'''CRIE UM PROGRAMA QUE LEIA A IDADE E O
SEXO DE VARIAS PESSOAS. A CADA PESSOA CADASTRADA
O PROGRAMA DEVERÁ PERGUNTAR SE O USUARIO QUER
OU NÃO CONTINUAR. NO FINAL MOSTRE:
A) QUANTAS PESSOAS TEM MAIS DE 18 ANOS;
B) QUANTOS HOMES FORAM CADASTRADOS;
C) QUANTAS MULHERES TEM MENOS DE 20 ANOS.'''

from time import sleep
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

maior = homens = mulher20 = pessoas = 0
while True:
    idade = int(input('DIGITE A IDADE...: '))
    sexo = str(input('DIGITE O SEXO...: ')).strip()[0].upper()
    while sexo not in 'FM':
        sexo = str(input(f'{branco}OPÇÃO INVÁLIDA...{fimdacor} DIGITE O SEXO {branco}[M/F]{fimdacor} ')).strip()[0].upper()
    pessoas += 1
    if idade >=18:
        maior +=1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    continua = str(input('DESEJA CONTINUAR? [S/N] ')).strip()[0].upper()
    while continua not in 'SN':
        continua = str(input(f'{branco}OPÇÃO INVÁLIDA...{fimdacor} DESEJA CONTINUAR? {branco}[S/N]{fimdacor} ')).upper().strip()[0]
    if continua == 'N':
        break
    print('-=' * 15)
    print('{}{:^30}{}'.format(branco,'NOVO CADASTRO',fimdacor))
    print('-=' * 15)
print('-=' * 15)
print(f'{azulc}ANALIZANDO OS DADOS...{fimdacor}')
print('-=' * 15)
sleep(1)
print('{}TOTAL DE PESSOAS CADASTRADAS . . . . . . {}{}{}'.format(branco, amarelo, pessoas, fimdacor))
print('{}TOTAL DE PESSOAS COM MAIS DE 18 ANOS . . {}{}{}'.format(branco, amarelo, maior, fimdacor))
print('{}TOTAL DE HOMENS CADASTRADOS. . . . . . . {}{}{}'.format(branco, amarelo, homens, fimdacor))
print('{}MULHERES COM MENOS DE 20 ANOS. . . . . . {}{}{}'.format(branco, amarelo, mulher20, fimdacor))