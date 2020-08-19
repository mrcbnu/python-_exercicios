###########################################
#              EXERCICIO 038              #
###########################################
'''ESCREVA UM PROGRAMA QUE LEIA DOIS NUMEROS
INTEIROS E COMPARE-OS, MOSTRANDO NA TELA UMA
 MENSAGEM:
 - O PRIMEIRO VALOR É MAIOR;
 - O SEGUNDO VALOR É MAIOR;
 - NÃO EXISTE MAOIR VALOR, OS DOIS SÃO IGUAS
 '''

print('\033[1;30m*\033[m' * 58)
print('', '\033[7;1;30m ' * 5, 'C O M P A R A D O R   D E   N U M E R O S', ' \033[7;1;30m' * 7, '\033[m')
print('\033[1;30m*\033[m' * 58)
n1 = int(input('DIGITE UM NUMERO......: '))
n2 = int(input('DIGITE OUTRO NUMERO...: '))
if n1 > n2:
    print('O PRIMEIRO NUMERO DIGITADO É MAIOR! {} > {}'.format(n1, n2))
elif n1 < n2:
    print('O SEGUNDO NUMERO DIGITADO É MAIOR! {} < {}'.format(n1, n2))
else:
    print('OS NUMEROS DIGITADOS SÃO IGUAIS! {} = {}'.format(n1, n2))
