###########################################
#              EXERCICIO 031              #
###########################################
'''DESENVOLVA UM PROGRAMA QUE PERGUNTE A
DISTANCIA DE UMA VIAGEM EM KM. CALCULE O
PREÇO DA PASSAGEM COBRANDO R$0,50 POR KM
PARA VIAGENS ATE 200KM E R$0,45 PARA
VIAGENS MAIS CURTA'''

dist=int(input('Qual a distancia (km) do seu destino?...:'))
if dist <= 200:
    print('O valor da passagem fica R$ {:.2f}'.format(dist*0.50))
else:
    print('O valor da passagem fica R$ {:.2f}'.format(dist*0.45))

