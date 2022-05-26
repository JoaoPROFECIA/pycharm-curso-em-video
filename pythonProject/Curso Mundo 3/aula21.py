#def fatorial(n=1):
#    if n == 0:
#        return 1
#    else:
#        return n * fatorial(n - 1)


#f1 = fatorial(5)
#f2 = fatorial(4)
#f3 = fatorial()
#print(f'Os valores são {f1}, {f2} e {f3}')


#def parOuImpar(n=0):
#    if n % 2 == 0:
#        return 'par'
#    else:
#        return 'impar'


#num = int(input('Digite um número: '))
#print(f'O número {num} é {parOuImpar(num)}')


def votoObrigatorio(ano=0):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - ano
    if idade < 16:
        return f'Com {idade} anos, não vota.'
    elif idade >= 16 and idade < 18 or idade > 65:
        return f'Com {idade} anos, vota opcional.'
    else:
        return f'Com {idade} anos, vota obrigatório.'


nasc = int(input('Ano de nascimento: '))
print(votoObrigatorio(nasc))
