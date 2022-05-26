def votoObrigatorio(ano):
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
