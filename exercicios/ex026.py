#############################################
#            EXERCICIO 026                  #
#############################################
'''FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
QUANTAS VEZES APARECE A LETRA 'A';
EM QUE POSIÇÃO ELA APARECE PELA PRIMEIRA VEZ;
EM QUE POSIÇÃO ELA APARECE PELA ULTIMA VEZ'''

frase = str(input('Digite uma frase: ')).upper().strip()
print('ANALIZANDO A FRASE ... {}'.format(frase))
print('A frase contem {} letra A\nA primeira letra A está na posição {}'
      '\nA ultima letra A esta na posição {}'.format(frase.count('A'), frase.find('A') + 1, frase.rfind('A') + 1))