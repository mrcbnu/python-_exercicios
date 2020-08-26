#! author: Marcio Alves


from lib.interface.layout import *
from lib.arquivos.arquivo import *

arq = 'dados.txt'
if arqExiste('dados.txt'):
    print('Arquivo encontrado com sucesso')
else:
    print('arquivos não encontrado')
    criarArquivo(arq)

while True:
    opção = menu(['CADASTRO', 'CONSULTA', 'FIM'])
    if opção == 1:  # opção de cadastrar um novo registro
        entraDados(arq)
    elif opção == 2:
        leiaArquivo(arq)
    elif opção == 3:
        cabecalho('~', 'FINALIZANDO... VOLTE SEMPRE')
        break
    else:
        linha('-')
        cabecalho('-', 'OPÇÃO INVALIDA')
