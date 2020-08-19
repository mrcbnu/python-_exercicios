###########################################
#              EXERCICIO 097              #
###########################################
'''
Faça um programa que tenha uma função chamada
escreva(), que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho
adaptável.
'''

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

# FUNÇÕES #
def escreva(f):
    print(f'{branco}-' * (len(f)+4), f'{fimdacor}')
    print(f'{amarelo}  {frase}{fimdacor}')
    print(f'{branco}-' * (len(f)+4), f'{fimdacor}')


# PROGRAMA PRINCIPAL #
print(f'{branco}-' * 80, f'{fimdacor}')
print()
frase = str(input(f'{branco}DIGITE UMA FRASE...: {fimdacor}')).upper()
escreva(frase)