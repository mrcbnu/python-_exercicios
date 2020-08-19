###########################################
#              EXERCICIO 100              #
###########################################
'''
Faça um programa que tenha uma lista chamada
números e duas funções chamadas sorteia() e
somaPar(). A primeira função vai sortear 5
números e vai colocá-los dentro da lista e a
segunda função vai mostrar a soma entre todos
os valores pares sorteados pela função anterior.
'''
from time import sleep
from random import randint

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


def sorteia(lista):
    """
    -> SORTEIA 5 NUMEROS ENTRE 0 E 10.
    -> CADA NUMERO SORTEADO É INCLUIDO COMO ITEM DA LISTA
    :param lista: É A LISTA QUE VAI SER ARMAZENADO OS VALORES SORTEADOS
    :return: SEM RETORNO
    """
    print(f'{branco}SORTEANDO 5 VALORES DA LISTA{fimdacor}', end=' ')
    for c in range(0, 5):
        num = randint(0, 10)
        lista.append(num)
        print(f'{amarelo}{num}', end=' ')
        sleep(0.25)
    print(f'{branco}PRONTO!{fimdacor}')


def soma_par(lista):
    soma = 0
    for v in lista:
        if v %2 == 0:
            soma += v
    print(f'{branco}A SOMA DOS VALORES PARES DE {amarelo}{lista}{fimdacor}{branco} TEMOS:{amarelo} {soma}{fimdacor}')


# programa principal
numeros = []
sorteia(numeros)
soma_par(numeros)

