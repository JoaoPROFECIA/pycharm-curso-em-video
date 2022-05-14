print('SOMANDO VÁRIOS VALORES')
soma = n1 = total = 0
n1 = int(input('Digite um número [0 para parar]: '))
while n1 != 0:
    soma += n1
    total += 1
    n1 = int(input('Digite um número [0 para parar]: '))
print(f'Com {total} números o total somado foi {soma}')
