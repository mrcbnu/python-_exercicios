###########################################
#              EXERCICIO 051              #
###########################################
'''DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO
TERMO DE P.A. (PROGRASSAOA ARITMETICA). NO FINAL
MOSTRE OS 10 PRIMEIROS TERMOS'''

a = int(input('DIGITE O PRIMEIRO TERMO DE UMA P.A....:'))
r = int(input('DIGITE A RAZÃO DA P.A.................:'))
for c in range(1,11):
    print(a,end='-')
    a += r
print('. . . ')