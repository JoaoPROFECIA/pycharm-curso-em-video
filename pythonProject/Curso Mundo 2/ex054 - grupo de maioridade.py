print('GRUPO DE MAIORIDADE\n')
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1,8):
    nasc = int(input(f'Em que ano a {pessoas}º pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'''\nDas idade apresentadas: 
{totmaior} são maiores de idade e {totmenor} são menores de idade''')
