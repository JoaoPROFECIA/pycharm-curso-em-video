# Formatando Moedas em Python

import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 12%, temos {moeda.aumentar(p, 12, True)}')
print(f'Reduzindo 17%, temos {moeda.diminuir(p, 17, True)}')
