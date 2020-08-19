from random import randint
from time import sleep
white = '\033[1;30m'
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
purple = '\033[1;35m'
lightblue = '\033[1;36m'
gray = '\033[1;37m'
stopcolor = '\033[m'
print(f'{lightblue}=-={stopcolor}' * 10)
print(f'{purple}VAMOS JOGAR PAR OU ÍMPAR{stopcolor}')
print(f'{lightblue}=-={stopcolor}' * 10)
cont = contvencedor = soma = 0
computador = 0
while True:
    valor = int(input(f'{yellow}Diga um valor: {stopcolor}'))
    computador = randint(1, 22)
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input(f'{yellow}Par ou Ímpar? [P/I]: {stopcolor}')).strip()[0].upper()
    print(f'{gray}Computador se preparando...{stopcolor}')
    sleep(2)
    print(f'{green}3...{stopcolor}')
    sleep(1)
    print(f'{yellow}2...{stopcolor}')
    sleep(1)
    print(f'{red}1...{stopcolor}')
    sleep(1)
    print(f'{white}LÁ VAI!{stopcolor}')
    sleep(0.5)
    soma = valor + computador
    print(f'{yellow}-{stopcolor}' * 30)
    print(f'{blue}Você jogou {valor} e o computador jogou {computador}, dando um total de {soma}. ', end='')
    print(f'{blue}DEU PAR{stopcolor}' if soma % 2 == 0 else f'{blue}DEU ÍMPAR{stopcolor}')
    print(f'{yellow}-{stopcolor}' * 30)
    if escolha == 'P':
        if soma % 2 == 0:
            print(f'{blue}Você venceu!{stopcolor}')
            print(f'{purple}Vamos jogar novamente...{stopcolor}')
            print(f'{yellow}=-={stopcolor}' * 10)
            contvencedor += 1
        else:
            print(f'{red}Você perdeu!{stopcolor}')
            print(f'{yellow}=-={stopcolor}' * 10)
            print(f'{red}GAME OVER! Você venceu {contvencedor} vezes{stopcolor}')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print(f'{blue}Você venceu!{stopcolor}')
            print(f'{purple}Vamos jogar novamente...{stopcolor}')
            print(f'{yellow}=-={stopcolor}' * 10)
            contvencedor += 1
        else:
            print(f'{red} Você perdeu! {stopcolor}')
            print(f'{yellow}=-={stopcolor}' * 10)
            print(f'{red}GAME OVER! Você venceu {contvencedor} vezes{stopcolor}')
            break
    else:
        print(f'{gray}Escolha inválida!!!{stopcolor}')
        print(f'{gray}POR FAVOR, ESCOLHA ENTRE [P/I] Par ou Ímpar...{stopcolor}')