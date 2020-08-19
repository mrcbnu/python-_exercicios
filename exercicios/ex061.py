###########################################
#              EXERCICIO 061              #
###########################################
'''REFAÇA O DESAFIO 051, LENDO O PRIMEIRO TERMO
E A RAZÃO DE UMA "PA", MOSTRANDO OS 10 PRIMEIROS
TERMOS DA PROGRESSÃO USANDO O WHILE'''

a = int(input('DIGITE O PRIMEIRO TERMO DE UMA PA.: '))
r = int(input('DIGITE A RAZÃO DA PROGRESSÃO......: '))
c = a
while c <= 10:
    print(' {} -'.format(a),end='')
    a += r
    c += 1
print(' FIM')
