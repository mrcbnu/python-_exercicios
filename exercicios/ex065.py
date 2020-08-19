###########################################
#              EXERCICIO 065              #
###########################################
'''CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS
PELO TECLADO. NO FINAL DA EXECUÇÃO, MOSTRE A
MEDIA ENTRE TODOS OS NUMEROS E QUAL FOI O
MAIOR E O MENOR VALOR DIGITADO. O PROGRAMA
DEVE PERGUNTAR SE O USUARIO QUER OU NAO
CONTINUAR A DIGITAR VALORES'''

from time import sleep
media = 0
soma = 0
cont = 0
flag = False
while not flag:
    num = int(input('DIGITE UM NUMERO...: '))
    soma += num
    cont += 1
    resp = ''
    if cont == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    while resp != 'N' and resp != 'S':
        resp = str(input('DESEJA CONTINUAR? [S/N]: ')).upper()
        if resp == 'N':
            flag = True
            print('\nF I N A L I Z A N D O . . .\n')
            sleep(1)
        elif resp == 'S':
            sleep(0.25)
        else:
            print('OPÇÃO INVÁLIDA... TENTE NOVAMENTE')
media = soma / cont
print('VOCÊ DIGITOU {} NUMEROS E A MEDIA ENTRE OS NUMEROS FOI DE {}'.format(cont,media))
print(f'O MAIOR VALOR FOI {maior} E O MENOR FOI {menor}')

