print('SEPARADOR DE DIGITOS DE UM NUMERO\n')
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'\nAnalizando o número {num}'
      f'\nUnidade: {u}'
      f'\nDezana: {d}'
      f'\nCentena: {c}'
      f'\nMilhar: {m}')