###########################################
#              EXERCICIO 054              #
###########################################
'''CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO
DE SETE PESSOAS. NO FINAL, MOSTRE QUANTAS PESSOAS
SÃO MENORES E QUANTAS SÃO MAIORES DE IDADE'''

from datetime import date
maior = 0
menor = 0
for cont in range (1, 8):
    ano = int(input('DIGITE O ANO DE  NASCIMENTO DA {}ª PESSOA:'.format(cont)))
    idade = date.today().year - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('{} pessoas são menores de 18 anos e {} são maiores de 18 anos'.format(menor,maior))