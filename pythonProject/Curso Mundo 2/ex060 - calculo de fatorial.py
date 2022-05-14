print('CALCULO DE FATORIAL\n')
'''import math
fat = int(input('Digite um número para calcular seu fatorial: '))
resultado = math.factorial(fat)
print(f'O fatorial de {fat} é {resultado}')'''
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end ='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -=1
print(f'{f}')