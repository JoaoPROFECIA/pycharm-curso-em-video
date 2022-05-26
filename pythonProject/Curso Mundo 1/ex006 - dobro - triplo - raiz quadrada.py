print('DOBRO - TRIPLO - RAIZ QUADRADA\n')
n = int(input('Digite um número: '))
#print(f'\nO dobro de {n} vale {n * 2}, o triplo vale {n * 3} e a raiz quadrada vale {n ** (1/2):.2f}.')

def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


def raiz(n):
    return n ** (1/2)


print(f'\nO dobro de {n} vale {dobro(n)}, o triplo vale {triplo(n)} e a raiz quadrada vale {raiz(n):.2f}.')
