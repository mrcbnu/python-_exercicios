# -------------------------------------------------#
#              EXERCICIO 19                       #
# -------------------------------------------------#
# um professor quer sortear um dos seu alunos para
# apagar o quadro.Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido

import random
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('Aluno escolhido: {}'.format(escolhido))

