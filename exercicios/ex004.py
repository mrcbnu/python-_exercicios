# -------------------------------------------------#
#              EXERCICIO 04                       #
# -------------------------------------------------#
# Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações
# possiveis sobre ela

print('--------------------------------------------')  # CABEÇALHO
print('           EXERCICIO 04                     ')  # DO
print('--------------------------------------------')  # EXERCICIO

resp = input('DIGITE ALGO...:')
print('O VALOR QUE VOCE DIGITOU...:')
print('O TIPO PRIMITIVO É: ',type(resp))
print('É UM NUMERO?',resp.isnumeric())
print('É ALFABETICO?',resp.isalpha())
print('É ALFANUMERICO? ',resp.isalnum())
print('ESTÁ EM MAIUSCULA? ',resp.isupper())
print('ESTÁ EM MINUSCULA? ',resp.islower())
print('ESTA CAPITALIZADA? ',resp.istitle())