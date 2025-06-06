def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO@ Digitacao errada, tente novamente. \033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mNao foi digitado um valor pelo usuario \033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO@ Digitacao errada, tente um numero real valido. \033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu nao digitar um valor para o usuario. \033[m')
            return 0
        else:
            return n




m1 = leiaInt(f'Digite um inteiro: ')
m2 = leiaFloat(f'Digite um Real: ')

print(f'O valor digitado inteiro digitado {m1} o valor real digitado: {m2}')
