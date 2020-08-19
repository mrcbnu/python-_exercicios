###########################################
#               EXERCICIO 023             #
###########################################
'''FAÇA UM PROGRAMA QUE LEIA UM NUMERO DE 0 A 9999
E MOSTRE NA TELA CADA UM DOS DIGITOS SEPARADAMENTE
EX:  1834 - UNI=4 DEZ=3 CEN=8 MIL=1'''

num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando o numero {}'.format(num))
print('Unidade = {}\nDezena  = {}\nCentena = {}\nMilhar  = {}'.format(u,d,c,m))




