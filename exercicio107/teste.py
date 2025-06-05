import moeda

p = float(input('Digite um numero'))
print(f'A metade do numero {p} é {moeda.metade(p)}')
print(f'O Dobro de R${p}, temos R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.dobro(p,10)}')
