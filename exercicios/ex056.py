###########################################
#              EXERCICIO 056              #
###########################################
'''DESENVOLVA UM PROGRAMA QUE LEIA O NOME,
IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA MOSTRE:
- MEDIA DE IDADE DO GRUPO;
- QUAL O NOME DO HOME MAIS VELHO;
- QUANTAS MULHERES TEM MENOS DE 20 ANOS.'''

soma_idade = 0
qdade_mulher = 0
idade_homem = 0
media = 0
soma_mulher = 0
nome_homem = ''
for pessoa in range(1,5):
    print('{}ª PESSOA'.format(pessoa))
    nome = str(input('NOME..........:')).upper().strip()
    idade = int(input('IDADE ........:'))
    sexo = str(input('SEXO (M/F) ...:')).upper().strip()
    soma_idade += idade
    if sexo == 'M':
        if idade > idade_homem:
            idade_homem = idade
            nome_homem = nome
    else:
        if idade < 20:
            soma_mulher += 1
media = soma_idade / pessoa
print('A MEDIA DE IDADE DO GRUPO É {:.2f} ANOS DE IDADE'.format(media))
print('{}, É O NOME DO HOMEM MAIS VELHO COM {} ANOS DE IDADE'.format(nome_homem,idade_homem))
print('{} MULHERES TEM MENOS DE 20 ANOS DE IDADE'.format(soma_mulher))
