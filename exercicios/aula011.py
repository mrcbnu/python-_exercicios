temp = {}
cadastro = [{'nome': 'MARCIO', 'idade': 42, 'sexo': 'MASCULINO', 'altura': 1.73},
            {'nome': 'JEICY', 'idade': 39, 'sexo': 'FEMININO', 'altura': 1.7},
            {'nome': 'JOÃO', 'idade': 7, 'sexo': 'MASCULINO', 'altura': 1.0}]
amarelo = {'amarelo':'\033[1;7;4;33m',
           'limpa': '\033[m'}
while True:
    temp['nome'] = str(input('NOME............:')).upper()
    temp['idade'] = int(input('IDADE..........:'))
    sexo = ' '
    while sexo not in 'fFMm':
        sexo = str(input('SEXO......[M/F]:')).upper()
    if sexo == 'M':
        temp['sexo'] = 'MASCULINO'
    else:
        temp['sexo'] = 'FEMININO'
    temp['altura'] = float(input('ALTURA.....:'))
    print(temp)
    resp = ' '
    cadastro.append(temp.copy())
    temp.clear()
    while resp not in 'NnSs':
        resp = str(input('DESEJA CONTINUAR [S/N]..:')).upper().strip()
    if resp == 'N':
        break
print('-'*55)
print(' CODIGO | NOME         | IDADE   | SEXO       | ALTURA')
print('-'*55)
for indice, valor in enumerate(cadastro):
    print(f' {indice + 1:^7}| {valor["nome"]:<13}| {valor["idade"]:<8}|'
          f' {valor["sexo"]:<11}| {valor["altura"]:<6.2f}')
