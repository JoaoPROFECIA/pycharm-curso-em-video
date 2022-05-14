import os

while 1:
    print('''Bem vindo ao converte!\n
    Digite o número da opção desejada:
    1- Converter de dólar para real
    2- Converter de real para dólar
    3- Sair''')
    opcao = int(input('\nDigite aqui: '))
    if opcao == 1:
        dolar = float(input('Qual a cotação atual do dólar em reais? '))
        valor = float(input('Qual o valor em dólar do produto que você deseja converter para reais? '))
        total = dolar * valor
        print('Seu valor em reais fica: R$ %.2f.' % total)
        input('Pressione qualquer tecla para continuar')

    if opcao == 2:
        dolar = float(input('Qual a cotação atual do dólar em reais? '))
        valor = float(input('Qual o valor em reais do produto que você deseja converter para dólares? '))
        total = valor / dolar
        print('Seu valor em dólares fica: U$ %.2f.' % total)
        input('Pressione qualquer tecla para continuar')
    if opcao == 3:
        print('Encerrando.......')
        break