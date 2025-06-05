'''
 Adapte o código do desafio #107,
  criando uma função adicional chamada moeda() que consiga mostrar os números como
  um valor monetário formatado.
'''
import moeda

p = float(input('Digite um numero'))
print(f'A metade do numero {p} é {moeda.metade(p)}')
print(f'O Dobro de R${p}, temos R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p,10)}')
