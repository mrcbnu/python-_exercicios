######################################
#          EXERCICIO 025             #
######################################
''' CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA
E DIGA SE ELA TEM SILVA NO NOME'''

nome = str(input('Digite seu nome: ')).upper().strip()
print('Você tem SILVA no seu nome? {}'.format('SILVA'in nome))