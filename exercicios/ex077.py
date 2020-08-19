###########################################
#              EXERCICIO 077              #
###########################################
'''Crie um programa que tenha uma tupla com
várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada
palavra, quais são as suas vogais.'''

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

palavras = ('exercicio', 'apoiador', 'acessando', 'professor', 'pavavras',
            'comentar', 'lapiseira', 'calculadora', 'anticonstitucionalissimamente')
for p in palavras:
    print(f'\nAs vogais da palavra {branco}{p}{fimdacor} são:', end=' ')
    for vogal in p:
        if vogal.upper() in 'AEIOU':
            sleep(0.25)
            print(f'{azulc}{vogal.upper()}{fimdacor}', end=' ')
print('\nFIM')
