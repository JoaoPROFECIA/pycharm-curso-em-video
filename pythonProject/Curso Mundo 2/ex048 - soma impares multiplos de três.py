print('SOMA ÍMPARES MÚLTIPLOS DE TRÊS\n')
soma = 0
cont = 0
for a in range(1, 501, 2):
    if a % 3 == 0:
        cont += 1
        soma = soma + a
print(f'A soma de todos os {cont} valores solicitados é {soma}')
