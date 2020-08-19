# -------------------------------------------------#
#              EXERCICIO 10                       #
# -------------------------------------------------#
# Faça um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dolares ela pode comprar

r = float(input('Digite quantos R$ voce tem na carteira...:'))
d = float(input('Digite a cotação do US$ hoje...: '))
c = r/d
print('com R$ {:.2f} , você consegue comprar US$ {:.2f}'.format(r,c))
