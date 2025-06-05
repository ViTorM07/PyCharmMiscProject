'''
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote
e mantenha tudo funcionando.
'''
from exercicio111.utilidadesCev import moeda
from exercicio111.utilidadesCev import dado

p = float(input('Digite um preço '))
moeda.resumo(p,20,12)