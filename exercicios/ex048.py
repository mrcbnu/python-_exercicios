###########################################
#              EXERCICIO 048              #
###########################################
'''FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE
OS NUMEROS IMPARES QUE SÃO MULTIPLOS DE 3 QUE
SE ENCONTRAM NO INTERVALO DE 1 A 500 '''

soma = 0
cont = 0
for n in range(0, 501):
    if n %2 !=0 and n % 3 == 0:
        print(soma,'+',n, '=', end=' ')
        soma += n
        cont += 1
        print(soma)
print('A SOMA DOS {} NUMEROS IMPARES E MULTIPLOS DE 3 ENTRE 0 E 500 É {}'.format(cont,soma))