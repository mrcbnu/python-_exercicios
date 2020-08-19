# -------------------------------------------------#
#              EXERCICIO 12                       #
# -------------------------------------------------#
# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço com 5% de desconto

preço = float(input('Digite o preço do produto...: '))
valor = preço - (preço * 5 / 100)
print('O valor do produto com 5% de desconto é...: R${:.2f}'.format(valor))
