###########################################
#              EXERCICIO 105              #
###########################################
"""
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
"""


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


def notas(*n, sit=False):
    lnotas = []
    dnotas = {}
    cont = 0

    # entrada das notas
    while True:
        cont += 1
        n = float(input(f'Digite a {cont}ª nota: '))
        lnotas.append(n)
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Deseja inserir mais notas [S/N] ')).upper()[0]
        if resp == 'N':
            break
    # tratamento dos dados
    dnotas['Qdade'] = len(lnotas)
    dnotas['Maior'] = max(lnotas)
    dnotas['Menor'] = min(lnotas)
    dnotas['Media'] = sum(lnotas) / len(lnotas)
    '''resp = ' '
    while resp not in 'SN':
        resp = str(input ('Deseja ver a situação geral da turma [S/N] ')).upper()[0]'''
    if sit:
        if dnotas['Media'] < 5:
            dnotas['Situação'] = 'RUIM'
        elif dnotas['Media'] < 7:
            dnotas['Situação'] = 'REGULAR'
        else:
            dnotas['Situação'] = 'BOA'
    print(lnotas)
    return dnotas


dnotas = notas(sit=True)
print(dnotas)
