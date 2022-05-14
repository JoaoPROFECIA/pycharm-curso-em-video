print('CONVERSOR DE BASES NUMÉRICAS\n')
while 1:
    print('''Escolha uma das bases para conversão: 
    1 - Converter para binário
    2 - converter para octal
    3 - converter para hexadecimal
    4 - Sair''')
    opcao = int(input('Sua opção: '))
    if opcao == 1 or opcao == 2 or opcao == 3:
        num = int(input('Digite um número inteiro: '))
        if opcao == 1:
            print(f'{num} convertido para binário é igual a {bin(num)[2:]}\n'
                  f'Pressione Enter para recomeçar')
        elif opcao == 2:
            print(f'{num} convertido para octal é igual a {oct(num)[2:]}\n'
                  f'Pressione Enter para recomeçar')
        elif opcao == 3:
            print(f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}\n'
                  f'Pressione Enter para recomeçar')
    elif opcao == 4:
        break
    else:
        print('Opção inválida. Tente novamente.\n'
              'Pressione Enter para recomeçar')
    input()
