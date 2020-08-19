###########################################
#              EXERCICIO 059              #
###########################################
'''CRIE UM PROGRAMA QUE LEIA DOIS VALORES E
MOSTRE NA TELA:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR'''

from time import sleep
n1 = int(input('DIGITE O PRIMEIRO NUMERO......: '))
n2 = int(input('DIGITE O SEGUNDO NUMERO.......: '))
menu = '\n\033[1;7;30m MENU PRINCIPAL \033[m\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NUMEROS\n[5] FATORIAL\n[6] SAIR'
opção = 0
fat = 0
while opção != 6:
    print(menu)
    opção = int(input('\033[1;30mQUAL A SUA OPÇÃO...: \033[m'))
    if opção == 1:
        print('\033[1;7;30m VAMOS SOMAR OS NUMEROS \033[m')
        totsoma = n1 + n2
        print('\033[1;30m{} \033[1;32m+ \033[1;30m{} \033[1;32m= \033[1;30m{}\033[m'.format(n1,n2,totsoma))

    elif opção == 2:
        print('\033[1;7;30m VAMOS MULTIPLICAR OS NUMEROS \033[m')
        totmult = n1 * n2
        print('\033[1;30m{} \033[1;32m* \033[1;30m{} \033[1;32m= \033[1;30m{}\033[m'.format (n1, n2, totmult))

    elif opção == 3:
        print('\033[1;7;30m VAMOS ANALIZAR QUAL É O MAIOR NUMERO \033[m')
        if n1 > n2:
            print('\033[1;30mO PRIMEIRO NUMERO É MAIOR QUE O SEGUNDO : {} > {}\033[m'.format(n1,n2))
        elif n2 > n1:
            print('\033[1;30mO SEGUNDO NUMERO É MAIOR QUE O PRIMEIRO : {} < {}\033[m'.format(n1, n2))
        else:
            print('\033[1;30mOS DOIS NUMEROS SÃO IGUIAS : {} = {}\033[m'.format (n1, n2))

    elif opção == 4:
        print('\033[1;7;30mINSIRA NOVOS NUMEROS\033[m')
        n1 = int(input('DIGITE O PRIMEIRO NUMERO...: '))
        n2 = int(input('DIGITE O SEGUNDO NUMERO....: '))
    elif opção == 5:
        f1 = n1
        anterior1 = f1 - 1
        print('\033[1;7;30m FATORIAL DO PRIMEIRO NUMERO: {}! \033[m'.format(n1))
        print('{} '.format(f1),end='')
        while anterior1 != 0:
            f1 = f1 * anterior1
            print('x {} '.format(anterior1), end='')
            anterior1 = anterior1 - 1
        print('= {}'.format(f1))
        f2 = n2
        anterior2 = f2 -1
        print('\033[1;7;30m FATORIAL DO SEGUNDO NUMERO: {}! \033[m'.format(n2))
        print('{} '.format(f2), end='')
        while anterior2 != 0:
            f2 = f2 * anterior2
            print('x {} '.format(anterior2), end='')
            anterior2 = anterior2 - 1
        print('= {}'.format(f2))
    elif opção == 6:
        print('FINALIZANDO .',end='')
        sleep(0.5)
        print(' .',end='')
        sleep(0.5)
        print(' .',end='')
        sleep(0.5)
        print(' .',end='')
        sleep(0.5)
    else:
       print('OPÇÃO INVÁLIDA... TENTE NOVAMENTE ')
print('\n\033[1;7;30m OBRIGADO! VOLTE SEMPRE \033[m')

