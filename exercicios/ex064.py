###########################################
#              EXERCICIO 064              #
###########################################
'''CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS
PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO
O USUARIO DIGITAR O VALOR 999, QUE É A CONDIÇÃO
DE PARADA. NO FINAL MOSTRE QUANTOS NUMEROS
FORAM DOGITADOS E QUAL A SOMA ENTRE ELES
(DESCONSIDERANDO O FLAG)'''

cont = 0
soma = 0
flag = False
while not flag:
    num = int(input('DIGITE UM NUMERO QUALQUER OU 999 PARA SAIR: '))
    if num == 999:
        flag = True
    else:
        soma = soma + num
        cont += 1
print('VOCÊ DIGITOU {} NUMEROS E A SOMA ENTRE ELES É {}'.format(cont,soma))