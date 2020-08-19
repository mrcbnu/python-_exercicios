###########################################
#              EXERCICIO 032              #
###########################################
'''FAÇA UM PROGRAMA QUE LEIA UM ANO E DIGA
SE ELE É UM ANO BISSEXTO'''

from datetime import date
ano = int(input('Digite um ano e descubra se ele é BISSEXTO, para ano atual digite 0...: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))