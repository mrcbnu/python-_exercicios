# -------------------------------------------------#
#              EXERCICIO 18                       #
# -------------------------------------------------#
# faça um programa que leia um angulo qualquer
# e mostre na tela seu seno, cosseno e tangente desse angulo

from math import sin, cos, tan, radians
a = float(input('digite um angulo qualquer: '))
se = sin(radians(a))
co = cos(radians(a))
ta = tan(radians(a))
print('Angulo {}°\nSeno {:.2f}\nCosseno {:.2f}\nTangente {:.2f}'.format(a,se,co,ta))
