###########################################
#              EXERCICIO 063              #
###########################################
'''ESCREVA UM PROGRAMA QUE LEIA UM NUMERO N
INTEIRO E MOSTRE NA TELA O N PRIMEIROS ELEMENTOS
DE UMA SEQUENCIA DE FIBONACCI'''

num = int(input('DIGITE O NUMERO ITENS DA SEQUENCIA DE FIBONACCI..: '))
atual = 1
anterior = 1
cont = 1
print('0 - ',end='')
while cont < num:
    print('{} - '.format(anterior),end='')
    atual = atual + anterior
    anterior = atual - anterior
    cont += 1
print('fim')
