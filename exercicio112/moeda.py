''''
:param preco
´:para, taxa
:param format
return 
'''''
def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato else moeda(res)

def diminuir(preco=0,taxa=0, formato =False):
    res = preco - (preco * taxa / 100)
    return res if not formato else moeda(res)

def dobro(preco=0, formato =False):
    res = preco *2
    return res if not formato else moeda(res)

def metade(preco=0, formato =False):
    res = preco / 2
    return res if not formato else moeda(res)

def moeda(preco =0, moeda ='R$'):
    return f'R$ {moeda} {preco:>.2f}'.replace('.','.')

def resumo(preco=0, taxaa=10, taxar=5 ):
    print('-='*30)
    print('RESUMO DO VALOR'.center(30))
    print('-='*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do R$\t{dobro(preco,True)}')
    print(f'Metade do R$\t{metade(preco,True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco,taxaa,True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preco,taxar,True)}')
    print('-='*30)