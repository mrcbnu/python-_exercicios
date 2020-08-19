###########################################
#              EXERCICIO 073              #
###########################################
'''CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS
COLOCADOS DA TABELA DO CAMPEONATO BRASILEIRO NA
ORDEM DE COLOCAÇÃO. DEPOIS MOSTRE:
A) OS 5 PRIMEIROS TIMES;
B) OS 4 ULTIMOS COLOCADOS;
C) TIMES EM ORDEM ALFABETICA;
D) EM QUE POSIÇÃO ESTA SEU TIME.'''

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

print(f'{branco}*{fimdacor}' * 50)
print('{}{:^50}{}'.format(amarelo,'CLASSIFICAÇÃO DO CAMPEONATO BRASILEIRO 2019',fimdacor))
print(f'{branco}*{fimdacor}' * 50)
times = ('FLAMENGO', 'SANTOS', 'PALMEIRAS', 'GREMIO', 'ATHLETICO-PR', 'SÃO PAULO',
        'INTERNACIONAL', 'CORINTHIANS', 'FORTALEZA', 'GOIAS', 'BAHIA', 'VASCO',
        'ATLETICO-MG','FLUMINENSE', 'BOTAFOGO', 'CEARÁ', 'CRUZEIRO', 'CSA',
        'CHAPECOENSE', 'AVAI')
print(f'\n{branco}5 PRIMEIROS COLOCADOS DA TABELA{fimdacor}')
for c in range(0, 5):
    print(f'{c+1}º {times[c]}',end=' - ')
    sleep(0.50)
print(f'\n{branco}4 ULTIMOS COLOCADOS DA TABELA{fimdacor}')
for c in range(16, 20):
    print(f'{c+1}º {times[c]}',end=' - ')
    sleep(0.50)
print(f'\n{branco}TIMES EM ORDEM ALFABETICA{fimdacor}')
alfa = sorted(times)
for c in range(0, 20):
    print(f'{alfa[c]}',end=' - ')
clube = str(input(f'\n{branco}DIGA QUAL O SEU TIME E VEJA EM QUE POSIÇÃO ELE ESTÁ NO CAMPEONATO : {fimdacor}')).upper().strip()
print(f'O {branco}{clube}{fimdacor} está na {branco}{times.index(clube)+1}ª {fimdacor}posição')