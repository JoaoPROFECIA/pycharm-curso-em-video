print('SOMA DE PARES\n')
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
if cont > 1:
    plularidade = 'números pares'
elif cont == 1:
    plularidade = 'número par'
print(f'Você informou {cont} {plularidade} e a soma foi {soma}')
