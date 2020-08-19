###########################################
#              EXERCICIO 079              #
###########################################
'''Crie um programa onde o usuário possa digitar
vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores
 únicos digitados, em ordem crescente.  '''

from time import sleep
# TABELA DE CORES #
branco = '\033[1;30m'
branco_in = '\033[1;7;30m'
vermelho = '\033[1;31m'
vermelho_in = '\033[1;7;31m'
verde = '\033[1;32m'
verde_in = '\033[1;7;32m'
amarelo = '\033[1;33m'
amarelo_in = '\033[1;7;33m'
azul = '\033[1;34m'
roxo = '\033[1;35m'
azulc = '\033[1;36m'
azulc_in = '\033[1;7;36m'
cinza = '\033[1;37m'
fimdacor = '\033[m'

lista = [int(input('DIGITE UM NUMERO '))]
print(f'{amarelo}ADICIONADO COM SUCESSO!{fimdacor}')
while True:
    resp = str(input('DESEJA CONTINUAR [S/N] ')).upper().strip()
    while resp not in 'SN':
        resp = str(input(f'{vermelho}OPÇÃO INVALIDA...{branco}DESEJA CONTINUAR [S/N] {fimdacor}')).upper().strip()
    if resp == 'N':
        break
    else:
        temp = int(input('DIGITE UM NUMERO: '))
        for c in lista:
            while temp in lista:
                print(f'{amarelo_in} VOCÊ JÁ DIGITOU ESSE NUMERO ! ! ! NÃO ADICIONADO {fimdacor}')
                temp = int(input('DIGITE UM NUMERO: '))
        lista.append(temp)
        print(f'{amarelo}ADICIONADO COM SUCESSO!{fimdacor}')
print(f'\n{branco}ANALIZANDO OS NUMEROS DIGITADOS ', end=''),sleep(0.25)
print('. ', end=''), sleep(0.25)
print('. ', end=''), sleep(0.25)
print('. ', end=''), sleep(0.25)
print('. ', end=''), sleep(0.25)
print('. ', end=''), sleep(0.25)
print('. ', end=''), sleep(0.25)
print(f'{fimdacor}\n')
print(f'{amarelo}A LISTA EM ORDEM CRESCENTE FICOU:{branco} {sorted(lista)}{fimdacor}')



