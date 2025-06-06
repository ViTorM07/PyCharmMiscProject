'''
 Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
'''


import urllib.request
import urllib.error


try :
    site = urllib.request.urlopen('https://www.pudim.com.br/')
    if site.status == 200:
        print('Acessado com sucesso!')
except urllib.error.URLError:
    print('Deu erro, o pudim não está acessível no momento :(')
else:
    print('Finalmente o pudim está pronto')
    print(site.read())