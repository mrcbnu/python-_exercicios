###########################################
#              EXERCICIO 034              #
###########################################
'''ESCREVA UM PROGRAMA QUE PERGUNTE O SALARIO
DE UM FUNCIONARIO E CALCULE O VALOR DE SEU
AUMENTO: PARA SALARIO SUPERIORES A R$1250,00
CALCULE AUMENTO DE 10 %, PARA SALARIOS MENORES
OU IGUAIS, O AUMENTO E DE 15% '''

sal = float(input('Qual o seu salário atual...R$ '))
if sal <= 1250:
    nsal = sal + (sal * 15 / 100)
    print('Seu novo salário com 15% de aumento é R$ {:.2f}'.format(nsal))
else:
    nsal = sal + (sal * 10 / 100)
    print('Seu novo salário com 10% de aumento é R$ {:.2f}'.format(nsal))

