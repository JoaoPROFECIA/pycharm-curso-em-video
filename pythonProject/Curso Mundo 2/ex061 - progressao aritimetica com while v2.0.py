print('='*10)
print('10 TERMOS DE UMA PA')
print('='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} → ', end='')
    termo += razao
    cont += 1
#for c in range(primeiro, decimo + razao, razao):
#    print(f'{c}', end=' → ')
print('FIM')
