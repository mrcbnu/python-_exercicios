nome = str(input('Qual o seu nome? ')).upper()
if nome == 'MARCIO':
    print('\033[4;030mQue lindo nome!!!\033[m')
elif nome == 'PEDRO' or nome == 'JOÃO' or nome =='MARIA':
    print('\033[4;030mSeu nome é bem comum no Brasil!!!\033[m')
else:
    print('\033[2;30mSeu nome é bem normal\033[m')
print('Tenha um bom dia \033[1;033m{}\033[m !'.format(nome))