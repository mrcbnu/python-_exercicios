###########################################
#              EXERCICIO 042              #
###########################################
'''DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO
DE TRES RETAS E DIGA AO USUARIO SE ELES PODEM
FORMAR UM TRIANGULO E QUAL TIPO DE TRIANGULO
SERA FORMADO:
- EQUILATERO: TODOS OS LADOS IGUAIS;
- ISOCELES: DOIS LADOS IGUIAS;
- ESCALENO: TODOS OS LADOS DIFERENTES'''

print('*' * 30)
print('ANALIZADOR DE TRIANGULOS')
print('*' * 30)
a = float(input('Primeiro segmento.... '))
b = float(input('Segunto segmento..... '))
c = float(input('Terceiro segmento.... '))
print('')
if a < (b+c) and b < (a+c) and c < (a+b):
    print('\033[1;30mOs segmentos PODEM FORMAR um triangulo \033[4m',end='')
    if a == b and a == c and b == c:
        print('EQUILÁTERO')
    elif a != b and a != c and b != c:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('\033[1;30mOs segmento acima NÃO PODEM FORMAR um triangulo!')