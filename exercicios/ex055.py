###########################################
#              EXERCICIO 055              #
###########################################
'''FAÇA UM PROGRAMA QUE LEIA O PESO DE 5
PESSOAS. NO FINAL MOSTRE QUAL FOI O MAIOR
E O MENOR PESO'''

maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('PESO DA {}ª PESSOA: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('{} KG foi o menor peso e {} KG foi o maior'.format(menor,maior))

