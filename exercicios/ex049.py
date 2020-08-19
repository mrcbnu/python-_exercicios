###########################################
#              EXERCICIO 049              #
###########################################
'''REFAÇA O EX009, MOSTRANDO A TABUADA DE UM
NUMERO QUE O USUARIO ESCOLHER, SÓ QUE AGORA
USANDO UM LAÇO FOR'''

print('\033[1;30m=\033[m' * 58)
print('', '\033[7;1;32m ' * 20, 'T A B U A D A', ' \033[7;1;32m' * 20, '\033[m')
print('\033[1;30m=\033[m' * 58)
print('')
n = int(input('Qual tabuada você quer listar? '))
for c in range(0,11):
    r = n * c
    print('{}  x  {:2} =  {}'.format(n,c,r))
print('F I M')