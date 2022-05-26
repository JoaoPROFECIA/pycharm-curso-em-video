def validando_Entrada_de_Dados(valor=0):
    '''
    Esta função valida a entrada de dados.
    '''
    while True:
        try:
            valor = int(input('Digite um valor: '))
            print(f'O valor digitado foi {valor}')
            break
        except ValueError:
            print('\033[31mERRO! Digite um valor válido.\033[m')
    return valor


validando_Entrada_de_Dados(valor=0)
