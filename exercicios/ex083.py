###########################################
#              EXERCICIO 083              #
###########################################
'''Crie um programa onde o usuário digite uma
expressão qualquer que use parênteses. Seu
aplicativo deverá analisar se a expressão
passada está com os parênteses abertos e
fechados na ordem correta.'''

expressao = str(input('DIGITE UMA EXPRESSÃO MATEMATICA...: '))
lista = []
for c in expressao:
    if c == '(':
        lista.append('c')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append('c')
            break
if len(lista) > 0:
    print(f'{expressao} É UMA EXPRESSÃO INVALIDA ')
else:
    print(f'{expressao} É UMA EXPRESSÃO VALIDA')
