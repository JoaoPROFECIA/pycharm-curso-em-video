def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno com {larg} x {comp} é de {a}m²')


# Programa principal
print('Controle de terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
