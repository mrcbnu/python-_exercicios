###################################
#         EXERCICIO 024           #
###################################
'''CRIR UM PROGRAMA QUE LEIA O NOME DE UMA
CIDADE E DIGA SE ELA COMEÇA OU NÃO COM O
NOME 'SANTO' '''

cidade = str(input('Digite o nome da sua cidade: ')).strip().upper().split()
# entra com nome da cidade, retira espaços antes e depois, coloca em maiusculas e divide transformando cidade em lista
print('Sua cidade começa com SANTO? {}'.format('SANTO' in cidade[0]))
# procura SANTO na primeira posição [0] da lista cidade

