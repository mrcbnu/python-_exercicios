###########################################
#              EXERCICIO 035              #
###########################################
'''DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO
DE TRES RETAS E DIGA AO USUARIO SE ELES PODEM
FORMAR UM TRIANGULO'''
print('*' * 30)
print('ANALIZADOR DE TRIANGULOS')
print('*' * 30)
a = float(input('Primeiro segmento.... '))
b = float(input('Segunto segmento..... '))
c = float(input('Terceiro segmento.... '))
if a < (b+c) and b < (a+c) and c < (a+b):
    print('Os segmento PODEM FORMAR um triangulo!')
else:
    print('Os segmento acima NÃO PODEM FORMAR um triangulo!')

