###########################################
#              EXERCICIO 110              #
###########################################
"""
Adicione o módulo moeda.py criado nos desafios
anteriores, uma função chamada resumo(), que
mostre na tela algumas informações geradas
pelas funções que já temos no módulo criado
até aqui.
"""

from exercicios.ex110 import moeda

# TABELA DE CORES #
c = (
    '\033[m',        # 0 - sem cor
    '\033[1;30m',    # 1 - branco
    '\033[1;7;30m',  # 2 - branco_in
    '\033[1;31m',    # 3 - vermelho
    '\033[1;30;41m', # 4 - vermelho_in
    '\033[1;32m',    # 5 - verde
    '\033[1;7;32m',  # 6 - verde_in
    '\033[1;33m',    # 7 - amarelo
    '\033[1;7;33m',  # 8 - amarelo_in
    '\033[1;34m',    # 9 - azul
    '\033[1;35m',    # 10 - roxo
    '\033[1;36m',    # 11 - azulc
    '\033[1;7;36m',  # 12 - azul_in
    '\033[1;37m',    # 13 - cinza
    )


valor = float(input('Digite o preço: R$: '))
moeda.resumo(valor)
