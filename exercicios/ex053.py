###########################################
#              EXERCICIO 053              #
###########################################
'''CRIE UM PROGRAMA QUE LEIA QUALQUER FRASE
E DIGA SE É UM POLINDROMO, DESCONSIDERANDO
OS ESPAÇOS'''

''' codigo sem FOR
frase = str(input('DIGITE UMA FRASE E VEJA SE É UM POLIDROMO:')).upper().replace(' ','')
if frase == frase[::-1]:
    print('o inverso de {} é {}, é um polidromo'.format(frase, frase[::-1]))
else:
    print ('o inverso de {} é {}, não é um polidromo'.format (frase, frase[::-1]))'''

''' CODIGO COM FOR'''

frase = str(input('DIGITE UMA FRASE E VEJA SE É UM POLIDROMO:')).upper().strip().replace(' ','')
print(frase)
inverso = ''
for letra in range(len(frase) -1, -1, -1):
    inverso += frase[letra]
    print(inverso)
if inverso == frase:
    print('Temos um polindromo')
else:
    print('Não temos um polindromo')