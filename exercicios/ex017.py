# -------------------------------------------------#
#              EXERCICIO 17                       #
# -------------------------------------------------#
# crie um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triangulo retangulo, calcule
# e mostre o comprimento da hipotenusa

# codigo usando calculo simples do teorema de pitagoras
'''
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hi = (co ** 2 + ca ** 2) **(1/2)
print('Hipotenusa = {:.2f}'.format(hi))
'''

# calculo usando a importacão do modulo math, função hypot (calculo da hipotenusa)
from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
#hi = hypot(co, ca)
print('Hipotenusa: {:.2f}'.format(hypot(co,ca)))

