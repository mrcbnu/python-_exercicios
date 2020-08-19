# -------------------------------------------------#
#              EXERCICIO 15                       #
# -------------------------------------------------#
# Escreva um programa que pergunte a qdade de km rodados
# por um carro alugado e a qdade de dias pelo que ele foi alugado.
# calcule o preço a pagar sabendo que o carro custa
# R$ 60,00 por dia e R$0.15 por km rodado

da = int(input('Quantos dias alugados? '))
km = float(input('quantos km rodados '))
vtotal = (da *60 ) + (km * 0.15)
print('O valor a pagar pelo aluguel do carro em {} dias e rodados {:.0f} km é R${:.2f}'.format(da,km,vtotal))
