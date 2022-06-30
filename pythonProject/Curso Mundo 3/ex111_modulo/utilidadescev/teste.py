# Formatando Moedas em Python

from ex111_modulo.utilidadescev import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 20, 12)