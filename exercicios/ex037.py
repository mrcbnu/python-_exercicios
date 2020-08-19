###########################################
#              EXERCICIO 037              #
###########################################
'''ESCREVA UM PROGRAMA QUE LEIA UM NUMERO
INTEIRO QUALQUER E PEÇA PARA O USUARIO ESCOLHER
QUAL SERÁ A BASE DE CONVERSÃO:
1 BINARIO, 2 OCTA, 3 HEXA'''

print('\033[1;30m*\033[m'*58)
print('','\033[7;1;30m '*10,'C O N V E R S O R   D E   B A S E',' \033[7;1;30m'*10,'\033[m')
print('\033[1;30m*\033[m'*58)
num = int(input('DIGITE UM NUMERO: '))
print('ESCOLHA QUAL BASE PARA CONVERTER')
print('\033[1;30m[1] BINARIO\n[2] OCTA\n[3] HEXA\033[m')
opção=int(input('OPÇÃO: '))
if opção == 1:
    print('\033[1;30m{}\033[m convertido para BINARIO é \033[1;30m{}\033[m'.format(num,bin(num)[2:]))
elif opção == 2:
    print('\033[1;30m{}\033[m convertido para OCTAL é \033[1;30m{}\033[m'.format(num,oct(num)[2:]))
elif opção == 3:
    print('\033[1;30m{}\033[m convertido para HEXADECIMAL é \033[1;30m{}\033[m'.format(num,hex(num)[2:]))
else:
    print('\033[7;1;30mOpção inválida\033[m')

