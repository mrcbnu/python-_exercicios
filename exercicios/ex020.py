# -------------------------------------------------#
#              EXERCICIO 20                       #
# -------------------------------------------------#
# O mesmo professor do exercicio anterior quer sortear
# a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que ajude ele,
# lendo o nome deles e mostre a ordem sorteada

import random
c1 = 'Agnaldo'
c2 = 'Aldo'
c3 = 'Gabriel'
c4 = 'Rodrigo'
lista = [c1, c2, c3, c4]
random.shuffle(lista)
print('A ordem de apresentação é')
print(lista)