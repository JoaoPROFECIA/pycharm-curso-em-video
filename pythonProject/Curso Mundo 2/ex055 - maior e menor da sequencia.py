print('MAIOR E MENOR PESO LIDO\n')
#maior = 0
#menor = 0
lst = []
for p in range(1,6):
    peso = float(input(f'Peso da {p} pessoa: '))
    lst += [peso]
print(f'\nO maior peso lido foi de {max(lst)}'
      f'O menor peso lido foi de {min(lst)}')
#    if p == 1:
#        maior = peso
#        menor = peso
#    else:
#        if peso > maior:
#            maior = peso
#        if peso < menor:
#            menor = peso
#print(f'\nO maior peso lido foi de {maior}'
#      f'\nO menor peso lido foi de {menor}')
##print(f'{max(peso)}')