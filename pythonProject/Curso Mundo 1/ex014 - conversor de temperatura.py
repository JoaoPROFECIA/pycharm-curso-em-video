while 1:
    print('CONVERSOR DE TEMPERATURA\n')
    print('''Escolha um número:
    1 - ºC para ºF'
    2 - ºF para ºC
    3 - Sair''')
    opcao = float(input('\nDigite aqui: '))
    if opcao == 1:
        c = float(input('Digite uma temperatura em ºC: '))
        f = ((9*c)/5)+32
        print(f'\nA temperatura de {c:.1f}ºC corresponde à {f:.1f}ºF')
        input('Pressione Enter para continuar')
    if opcao == 2:
        f = float(input('Digite uma temperatura em ºF: '))
        c = ((f-32)*5)/9
        print(f'\nA temperatura de {f:.1f}ºF corresponde à {c:.1f}ºC')
        input('Pressione Enter para continuar')
    if opcao == 3:
        break