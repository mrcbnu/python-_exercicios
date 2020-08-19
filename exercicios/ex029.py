###########################################
#              EXERCICIO 029              #
###########################################
'''ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE
DE UM CARRO, SE ULTRAPASSAR 80KM/H MOSTRE
UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO
A MULTA CUSTA R$7,00 POR CADA KM ACIMA DO
LIMITE'''

print('*'*60)
print(' '*20,'R A D A R  M Ó V E L')
print('*'*60,'\n')
vel=int(input('VELOCIDADE AFERIDA....:'))
if vel > 80:
    print(' '*10, 'VOCE ULTRAPASSOU O LIMITE DE VELOCIDADE')
    print(' '*10, 'O valor da multa é de R$ {:.2f}'.format((vel - 80)*7))
else:
    print(' '*20, 'BOA VIAGEM')

