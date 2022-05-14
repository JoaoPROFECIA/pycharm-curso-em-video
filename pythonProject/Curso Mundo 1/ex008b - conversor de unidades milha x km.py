while 1:
    print('CONVERSOR DE UNIDADES: MILHA x KM\n')
    print('''Escolha um número:
          1- Milhas para km
          2 - Km para milhas''')
    opcao = int(input('Digite aqui: '))
    if opcao == 1:
        milhas = float(input('Quantas milhas? '))
        km = milhas * 1.60934
        print(f'\n{milhas} milhas valem {km:.2f}km')
        input('Pressione qualquer tecla para continuar\n\n')
    if opcao == 2:
        km = float(input('Quantos km? '))
        milha = km * 0.621371
        print(f'\n{km}km valem {milha:.2f} milhas')
        input('Pressione qualquer tecla para continuar\n\n')
