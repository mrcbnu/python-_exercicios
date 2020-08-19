###########################################
#              EXERCICIO 075              #
###########################################
'''Desenvolva um programa que leia quatro
valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

numeros = (int(input('DIGITE UM NUMERO ')), int(input('DIGITE OUTRO NUMERO ')),
           int(input('DIGITE OUTRO NUMERO ')), int(input('DIGITE OUTRO NUMERO ')))
print(f'{numeros}')
print(f'O NUMERO 9 APARECEU {numeros.count(9)} VEZES!')
if 3 in numeros:
    print(f'O PRIMEIRO NUMERO 3 ESTA NA POSIÇÃO {numeros.index(3)+1}')
else:
    print('NÃO FOI DADO ENTRADA NO MUMERO 3')
pares = 0
for n in numeros:
    if n % 2 == 0:
        print(f'{n}', end='  ')
        pares += 1
if pares == 0:
    print('NÃO HOUVE NUMEROS PARES')
elif pares == 1:
    print('É O NUMERO PAR')
else:
    print('SÃO OS NUMEROS PARES')
