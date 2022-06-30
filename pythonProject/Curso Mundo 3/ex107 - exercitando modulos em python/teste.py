import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 12%, temos {moeda.aumentar(p, 12)}')
print(f'Reduzindo 17%, temos {moeda.diminuir(p, 17)}')
