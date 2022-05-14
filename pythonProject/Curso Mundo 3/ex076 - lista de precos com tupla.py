print('LISTA DE PREÇOS COM TUPLAS\n')
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

lista = []
soma = cont = 0

while True:
    produto = str(input('Nome do produto: ')).upper().strip()
    valor = float(input('Preço: '))
    lista += produto, valor
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

    while continuar not in 'SN':
        continuar = str(input('Tente novamente. Quer continuar? [S/N]'))

    print('-='*18)
    print(f'{"LISTA DE PRODUTOS":^36}\n')

    for c in range(0, len(lista), 2):
        print(f'{lista[c]:.<25} R${lista[c + 1]:.2f}')
        cont += 1

    for c in range(1, len(lista), 2):
        soma += lista[c]

    if continuar in 'N':
        print()
        print(f'Você comprou {cont} produtos e a soma')
        print(f'deles foi de R${soma:.2f}')
        print('-=' * 18)
        break

    print()
    print(f'Você comprou {cont} produtos e a soma')
    print(f'deles foi de R${soma:.2f}')
    print('-=' * 18)

#lista = ('Lápis', 1.75,
#        'Borracha', 2,
#        'Caderno', 15.90,
#        'Estojo', 25.00,
#        'Transferidor', 4.20,
#        'Compasso', 9.99,
#        'Mochila', 120.32,
#        'Canetas', 22.30,
#        'Livro', 34.90)
#for posição in range(0, len(lista)):
#    if posição % 2 == 0:
#        print(f'{lista[posição]:.<30}', end='')
#    if posição % 2 == 1:
#        print(f'R${lista[posição]:>7.2f}')
#print('-'*40)
