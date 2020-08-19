###########################################
#              EXERCICIO 067              #
###########################################
'''FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE
VARIOS NUMEROS, UM DE CADA VEZ, PARA CADA
VALOR DIGITADO PELO USUARIO. O PROGRAMA SERÁ
INTERROMPIDO QUANDO O NUMERO SOLICITADO FOR
NEGATIVO'''

while True:
    num = int(input('DIGITE UM NUMERO E VEJA A SUA TABUADA: '))
    if num < 0:
        break
    for c in range(1,11):
        r = num * c
        print(f'{num}  x {c:2} = {r:2}')
    print('-' * 15)
print('FIM')