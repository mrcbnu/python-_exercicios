###########################################
#              EXERCICIO 100              #
###########################################
"""
Crie um programa que tenha uma função chamada
voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor
literal indicando se uma pessoa tem voto NEGADO,
OPCIONAL e OBRIGATÓRIO nas eleições.
"""
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


def voto(ano):
    """
    FUNÇÃO QUE VALIDA A IDADE DO ELEITOR
    :param ano: ano de nascimento
    :return: idade menor que 16 anos: NÃO VOTA
             idade entre 16 e 17 anos e acima de 65 anos: VOTO OPCIONAL
             idade entre 18 e 65: APTO A VOTAR
    """
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'{amarelo}COM {idade} ANOS: NÃO VOTA{fimdacor}'
    elif 16 <= idade < 18 or idade > 65:
        return f'{amarelo}COM {idade} ANOS: VOTO OPCIONAL{fimdacor}'
    else:
        return f'{amarelo}COM {idade} ANOS: APTO A VOTAR{fimdacor}'


print(f'{branco}-{fimdacor}' * 40)
print('{}{:^40}{}'.format(amarelo, 'ELEIÇÕES 2020', fimdacor))
print(f'{branco}-{fimdacor}' * 40, end='\n')
nasc = int(input(f'{branco}DIGITE O ANO DE NASCIMENTO DO ELEITOR....:{fimdacor} '))
print(voto(nasc))
help(voto)
