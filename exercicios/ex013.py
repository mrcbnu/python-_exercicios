# -------------------------------------------------#
#              EXERCICIO 13                       #
# -------------------------------------------------#
# Faça um algoritmo que leia o salario de um funcionario
# e mostre seu novo salario com 15% de aumento

salario = float(input('Digite se salario...: R$ '))
novo = salario + (salario * 15 / 100)
print('Seu salario com reajunste de 15% é R$ {:.2f}'.format(novo))
