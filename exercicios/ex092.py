###########################################
#              EXERCICIO 092              #
###########################################
''' Crie um programa que leia nome, ano de
nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário. Se por acaso a
CTPS for diferente de ZERO, o dicionário
receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos
anos a pessoa vai se aposentar.'''

from time import sleep
from datetime import date
from random import randint
from operator import itemgetter
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


cadastro = dict()

cadastro['nome'] = str(input('NOME..................: ')).upper()
ano_nasc = int(input('ANO DE NASCIMENTO..:'))
cadastro['idade'] = date.today().year - ano_nasc
cadastro['CTPS'] = int(input('CARTEIRA DE TRABALHO (0 se não tem)...: '))
if cadastro['CTPS'] != 0:
    cadastro['contratação'] = int(input('ANO DE CONTRATAÇÃO....: '))
    cadastro['salario'] = float(input('SALÁRIO......R$ '))
    cadastro['aposentar'] = (cadastro['contratação'] + 35) - ano_nasc
for k, i in cadastro.items():
    print(f'{k}  =  {i}')
print(cadastro)

