###########################################
#              EXERCICIO 066              #
###########################################
'''CRIE UM PROGRAMA QUE LEIA NUMEROS INTEIROS
PELO TECLADO. O PROGRAMA SÓ VAI PARA QUANDO O
USUARIO DIGITAR 999, QUE É A CONDIÇÃO DE PARADA
NO FINAL MOSTRE QUANTOS NUMEROS FORAM DIGITADOS
E QUAL A SOMA ENTRE ELES'''

cont = soma = 0
while True:
    num = int(input('Digite um numero, 999 para sair: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} e a soma entre eles foi {soma}')

