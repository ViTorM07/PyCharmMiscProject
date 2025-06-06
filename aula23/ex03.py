try:
    a = int(input('Numerador'))
    b = int(input('Denominador'))
    r = a/b
except(ValueError, TypeError):
    print(f'Infelizmente tivemos um problema com o tipo de dado, tente novamente.')
except ZeroDivisionError:
    print('Nao é possivel dividir por zero')
except KeyboardInterrupt:
    print('O usuario nao digitou nenhum valor')
except Exception as erro:
    print(f'Erro encontrado foi{erro.__cause__}')
else:
    print(f'O resultado é {r:1f}')
finally:
    print('Volte sempre, muito obrigado!')
