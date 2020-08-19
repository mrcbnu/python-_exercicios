##########################################
#              EXERCICIO 057              #
###########################################
'''FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA,
MAS SÓ ACEITE OS VALORES"M" OU "F". CASO ESTEJE
ERRADO PEÇA A DIGITAÇÃO ATÉ TER UM VALOR CORRETO'''

sexo = str(input('Digite o sexo [M/F] ')).upper()
if sexo != 'M' and sexo != 'F':
    while sexo != 'M' and sexo != 'F':
        print('Opção errada, digite novamente...')
        sexo = str(input('Digite o sexo [M/F]')).upper()
print('FIM')