def fatorial(n, show=False):
    '''
    -> Calcula o fatorial de um número.
    :para n: O número a ser calculado
    :para show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de n
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c != 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


num = int(input('Digite um número: '))
print(f'{num}\nO fatorial de {num} é {fatorial(num, show=True)}')
