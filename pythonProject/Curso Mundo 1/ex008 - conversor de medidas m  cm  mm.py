while 1:
    print('CONVERSOR DE MEDIDAS: M > CM > MM\n')
    print('''Escolha um número:
    1 - Metros para centímetros
    2 - Centímetros para Milímetros
    3 - Metros para Milímetros''')
    opcao = int(input('\nDigite aqui: '))
    if opcao == 1:
        metros = float(input('Qual é a metragem? '))
        centímetros = metros * 100
        print(f'{metros}m equivalem a {centímetros}cm')
        input('Pressione qualquer tecla para continuar\n\n')
    if opcao == 2:
        centímetros = float(input('Quantos centímetros? '))
        milímetros = centímetros * 10
        print(f'{centímetros}cm equivalem a {milímetros}mm')
        input('Pressione qualquer tecla para continuar\n\n')
    if opcao == 3:
        metros = float(input('Quantos metros? '))
        milímetros = metros * 1000
        print(f'{metros}m equivalem a {milímetros}mm')
        input('Pressione qualquer tecla para continuar\n\n')
