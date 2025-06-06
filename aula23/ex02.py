# try:
#     a = int(input('Numerador'))
#     b = int(input('Denominador'))
#     r = a/b
# except:
#     print(f'Infelizmente tivemos um problema, tente novamente.')
# else:
#     print(f'O resultado é {r:1f}')
# finally:
#     print('Volte sempre, muito obrigado!')
#Tambem posso
try:
    a = int(input('Numerador'))
    b = int(input('Denominador'))
    r = a/b
except Exception as erro:
    print(f'Infelizmente tivemos um problema, erro do tipo{erro.__class__}')
else:
    print(f'O resultado é {r:1f}')
finally:
    print('Volte sempre, muito obrigado!')


