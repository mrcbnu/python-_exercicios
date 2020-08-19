###########################################
#              EXERCICIO 046              #
###########################################
'''FAÇA UM PROGRAMA QUE MOSTRE NA TELA UM CONTAGEM
REGRESSIVA PARA O ESTOURO DE FOGOS DE ARTIFICIO,
INDO DE 10 A 0 COM PAUSA DE 1 SEGUNDO'''

import time
for c in range(10,-1,-1):
    print(c)
    time.sleep(1)
print('bumm .....   bumm ..... pow  ')

