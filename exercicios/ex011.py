# -------------------------------------------------#
#              EXERCICIO 11                       #
# -------------------------------------------------#
# Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule sua area, e a quantidade de tinta
# necessaria para pinta-la, sabendo que cada litro de tinta
# pinta uma area de 2m2

lar = float(input('Digite a largura da parede...:'))
alt = float(input('Digite a altura da parede ...:'))
area = alt * lar
tinta = area / 2
print('a quantidade de tinta necessaria para pintar uma parede de {:.2f} m2 é de {:.2f} litros'.format (area,tinta))
