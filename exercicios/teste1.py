import csv

with open('TESTE.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    csv_reader.__next__ ()
    print('{:^10}|{:^46}| {:^58}|'.format('NF-e', 'CHAVE NF-E', 'RAZÃO SOCIAL'))
    print('{:^10}|{:^46}| {:^58}|'.format('-' * 8, '-' * 44 , '-' * 57))
    for c in csv_reader:
        print('{:^10}|{:^46}| {:<58}|'.format(c[4], c[15],c[7]))
