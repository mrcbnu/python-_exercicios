###########################################
#              EXERCICIO 036              #
###########################################
'''ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO
BANCÁRIO PARA A COMPRA DE UMA CASA. O PROGRAMA
VAI PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR
E EM QUANTOS ANOS ELE VAI PAGAR.
CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE
ELA NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O
EMPRÉSTIMO SERÁ NEGADO'''
import time                         # IMPORTA MODULO DE TEMPO
print('\033[1;30m*\033[m'*50)
print('','\033[7;1;30m '*15,'A L V E S  B A N K',' \033[7;1;30m'*12,'\033[m')
print('\033[1;30m*\033[m'*50)
print('','\033[7;1;31m SIMULAÇÃO DE CRÉDITO IMOBILIÁRIO \033[m')
print('')
nome = str(input('NOME DO COMPRADOR: ')).upper()
vcasa = float(input('VALOR DO IMÓVEL R$: '))
salario = float(input('SALÁRIO DO COMPRADOR R$: '))
anos = int(input('TEMPO DE FINANCIAMENTO (ANOS): '))
parcelas = anos * 12                # CALCULA QDADE DE MESES
vparc = vcasa / parcelas            # CALCULA VALOR DA PARCELA
porsal = (vparc / salario) * 100    # CALCULA PORCENTAGEM DO SALARIO
print('-'*50)
print(' P R O C E S S A N D O   O S   D A D O S . . . ')
print('-'*50)
time.sleep(2)                       # ESPERA 2 SEGUNDOS
print('\033[30mSr(a) {}, o valor da parcela fica em {}x de R$ {:.2f}\033[m'.format(nome,parcelas,vparc))
time.sleep(2)                       # ESPERA 2 SEGUNDOS
if porsal <30:                      # SE PORCENTAGEM FOR MENOR QUE 30% DO SALÁRIO
    print('\n\033[30mO valor da parcela corresponte a {:.2f}% do seu salário'.format(porsal))
    print('-' * 53,'\n\033[1;30mF I N A N C I A M E N T O  A P R O V A D O\033[m')
    print('-' * 53)
else:                               # SENÃO PORCENTAGEM É MAIOR QUE 30% 
    print('\n\033[30mO valor da parcela corresponte a {:.2f}% do seu salário'.format(porsal))
    print('-' * 53, '\n\033[1;30mF I N A N C I A M E N T O   N Ã O   A P R O V A D O\033[m')
    print('-' * 53)

