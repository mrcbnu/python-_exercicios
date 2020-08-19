import urllib.request

try:
    site = urllib.request.urlopen("http://www.uol.com.br")
except:
    print('BUGOU!')
else:
    print('Tudo OK...')
