# -------------------------------------------------#
#              EXERCICIO 08                       #
# -------------------------------------------------#
# Faça um programa que leia um valor em metros
# e exiba convertido em centimetro e milimetros

mt = float(input('digite um distancia em metros...:'))
mm = mt * 1000
dm = mt * 10
cm = mt * 100
dam = mt / 10
km = mt / 1000
hm = mt / 100

print('{} metro(s) é {:.0f} centimetros e {:.0f} milimetros'.format(mt, cm, mm))
print('{} metro(s) é {} km e {} dam'.format(mt,km,dam))

