###########################################
#              EXERCICIO 072              #
###########################################
'''CRIE UM PROGRAMA QUE TENHA UMA TUPLA
TOTALMENTE PREENCHIDA COM UMA CONTAGEM
POR EXTENSO, DE ZERO ATÉ VINTE. SEU PROGRAMA
DEVERÁ LER UM NUMERO PELO TECLADO (0 A 20) E
MOSTRAR POR EXTENSO'''

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

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input(f'{branco}DIGITE UM NUMERO (0 A 20) E VEJA COMO ELE É POR EXTENSO...: {fimdacor}'))
    sleep(0.25)
    if num > 20:
        break
    print(f'O NUMERO {amarelo}{num}{fimdacor} POR EXTENSO É {amarelo}{extenso[num].upper()}{fimdacor}\n')
print(f'\n{branco_in} FIM {fimdacor}')



