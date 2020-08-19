#######################################
#              EXERCICIO 022          #
#######################################
'''CRIE UM PRIGRAMA QUE LEIA O NOME COMPLETO
 DE UMA PESSOA E MOSTRE:
 O NOME COM TODAS AS LETRAS MAIUSCULAS
 O NOME COM TODAS AS LETRAS MINUSCULAS
 QUANTAS LETRAS TEM O NOME (SEM CONSIDERAR OS ESPAÇOS)
 QUANTAS LETRAS TEM O PRIMEIRO NOME'''

nome = str(input('Digite se nome completo: ')).strip()
print('Analizando seu nome....')
print('Seu nome em letras maiusculas é {}'.format(nome.upper()))
print('Seu nome em letras minusculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras' .format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))

