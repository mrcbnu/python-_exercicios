######################################
#            EXERCICIO 027           #
######################################
'''FAÇA UM PROGRA QUE LEIA O MOME COMPLETO
SE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO
NOME O E ULTIMO NOME SEPARADAMENTE'''

nome = str(input('Digite seu nome completo: ')).upper().strip().split()
print('ANALIZANDO SEU NOME....')
print(len(nome))
print('Primeiro nome: {}'.format(nome[0]))
print('Ultimo nome: {}'.format(nome[len(nome)-1]))

