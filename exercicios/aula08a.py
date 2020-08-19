locadora = []
filme = {}
while True:
    filme['titulo'] = str(input('TITULO DO FILME...: ')).title()
    filme['ano'] = int(input('ANO DO FILME...: '))
    filme['diretor'] = str(input('DIRETOR...: ')).title()
    locadora.append(filme.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('DESEJA CONTINUAR [S/N]')).upper()
    if resp == 'N':
        break
print(locadora)



