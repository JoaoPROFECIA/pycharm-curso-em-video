print('MAIOR E MENOR VALOR EM UMA TUPLA\n')

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ', end='')

for n in numeros:
    print(f'{n} ', end=' ')

print(f'\nO maior valor digitado foi {max(numeros)}'
      f'\nO menor valor sorteado foi {min(numeros)}')
