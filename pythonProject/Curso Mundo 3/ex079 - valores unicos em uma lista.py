print('VALORES ÚNICOS EM UMA LISTA\n')

valores = []

while True:
    n = int(input('Digite um valor: '))

    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    continuar = ' '

    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        if continuar == 's':
            continue

    if continuar == 'n':
        break

print('-=' * 20)
valores.sort()
print(f'Você digitou os valores {valores}')
