###########################################
#              EXERCICIO 039              #
###########################################
'''FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO
DE UM JOVEM E INFORME DE ACORDO COM A SUA IDADE:
- SE ELE AINDA VAI SE ALISTAR;
- SE É A HORA DE SE ALISTAR;
- SE JÁ PASSOU O TEMPO DE ALISTAMENTO;
O PROGRAMA DEVER MOSTRAR O TEMPO QUE FALTA E O
TEMPO QUE PASSOU DO PRAZO
 '''

from datetime import date
data = date.today()
atual = date.today().year
print('\033[1;30m=\033[m' * 58)
print('', '\033[7;1;32m ' * 10, 'E X E R C I T O   N A C I O N A L', ' \033[7;1;32m' * 10, '\033[m')
print('\033[1;30m=\033[m' * 58)
print('\033[1;30m SETOR DE RECRUTAMENTO',' ' * 22, '{}\033[m\n'.format(data))
nome = str(input('NOME ................:')).upper()
data = int(input('ANO DE NASCIMENTO ...:'))
idade = atual - data
if idade == 18:
    print('\033[1;7;30mVOCÊ TEM {} DE IDADE E DEVE SE ALISTAR IMEDIATAMENTE\033[m'.format(idade))
elif idade < 18:
    dif = 18 - idade
    print('\033[1;7;32mVOCÊ TEM {} ANOS DE IDADE E AINDA FALTA {} ANOS PARA SE ALISTAR\033[m'.format(idade,dif))
else:
    dif = idade - 18
    print('\033[1;7;31mVOCÊ TEM {} ANOS DE IDADE E JÁ PASSOU {} ANOS PARA SE ALISTAR\033[m'.format(idade,dif))

