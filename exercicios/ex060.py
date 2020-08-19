###########################################
#              EXERCICIO 060              #
###########################################
'''FAÇA UM PROGRAMA QUE LEIA UM NUMERO QUALQUER
E MOSTRE SEU FATORIAL
EX 5! = 5 X 4 X 3 X 2 X 1 = 120'''

num = int(input('DIGITE UM NUMERO: '))
print('{}! = {} '.format(num, num), end='')
anterior = num - 1
while anterior != 0:
    num *= anterior
    print('x {} '.format(anterior),end='')
    anterior -= 1
print('= {}'.format(num))


