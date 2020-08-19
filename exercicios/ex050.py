###########################################
#              EXERCICIO 050              #
###########################################
'''DESENVOLVA UM PROGRAMA QUE LEIA 6 NUMEROS
INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE
FOREM PARES. SE O VALOR FOR IMPAR, DESCONSIDERE'''

soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite {}º numero: '.format(c)))
    if n %2 == 0:
        soma += n
        cont += 1
print('A SOMA DOS {} NUMEROS PARES QUE VOCÊ DIGITOU FOI {}'.format(cont,soma))