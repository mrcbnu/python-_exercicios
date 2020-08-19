###########################################
#              EXERCICIO 111              #
###########################################
"""
Crie um pacote chamado utilidadesCeV que tenha
dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios
107, 108 e 109 para o primeiro pacote e mantenha
tudo funcionando.
"""

from exercicios.ex111.utilidadesCeV import moeda
# TABELA DE CORES #
from exercicios.ex111.utilidadesCeV import leiaDinheiro

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


valor = leiaDinheiro(input('Digite o preço: R$: '))
moeda.resumo(valor)
