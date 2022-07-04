# Formatando Moedas em Python

from moeda import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 20, 12)