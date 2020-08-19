###########################################
#              EXERCICIO 062              #
###########################################
'''MELHORE O DESAFIO EX061, PERGUNTANDO PARA
O USUARIO SE ELE QUER MOSTAR MAIS ALGUNS TERMOS
O PROGRAMA ENCERRA QUANDO ELE DISSER QUE QUER
MOSTRAR 0 TERMOS'''

num = int(input('DIGITE O PRIMEIRO TERMO...:'))
razao = int(input('DIGITE A RAZÃO DA PA ....:'))
termos = int(input('DIGITE NUMERO DE TERMOS....:'))
cont = 0
total = termos
while termos != 0 and termos > cont:
    print('{}  '.format(num),end='')
    num += razao
    cont += 1
    if cont == termos:
        print('PAUSA')
        termos = int(input('VOCÊ GOSTARIA DE LISTAR MAIS QUANTOS TERMOS: '))
        total += termos
        cont = 0
print('\nPROGRAMA FINALIZADO, FOI MOSTRADO {} TERMOS'.format(total))


