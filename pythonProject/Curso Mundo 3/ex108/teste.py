# Formatando Moedas em Python

import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 12%, temos {moeda.moeda(moeda.aumentar(p, 12))}')
print(f'Reduzindo 17%, temos {moeda.moeda(moeda.diminuir(p, 17))}')
