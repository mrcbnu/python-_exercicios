# -------------------------------------------------#
#              EXERCICIO 14                       #
# -------------------------------------------------#
# Escreva um programa que comverta a temperatura
# digitando em graus celsius para fahrenheit

grauc = float(input('Digite a temperatura em °C :'))
grauf = ((grauc * 9) / 5) + 32
print('{}°C = {}°F'.format(grauc,grauf))
