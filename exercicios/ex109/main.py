###########################################
#              EXERCICIO 109              #
###########################################
"""
Modifique as funções que form criadas no
desafio 107 para que elas aceitem um parâmetro
a mais, informando se o valor retornado por elas
vai ser ou não formatado pela função moeda(),
desenvolvida no desafio 108..
"""

from exercicios.ex109 import moeda

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
print(f'{c[1]}A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}{c[0]}')
print(f'{c[7]}O dobro de  {moeda.moeda(valor)} é {moeda.dobro(valor, True)}{c[0]}')
print(f'{c[11]}Aumentado 10%, temos {moeda.aumentar(valor, 10, True)}{c[0]}')
print(f'{c[5]}Descontando 10%, temos {moeda.diminuir(valor, 10, True)}{c[0]}')
