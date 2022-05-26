print('ANO BISSEXTO\n')
from datetime import date
#ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
#if ano == 0:
#    ano = date.today().year
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#    print(f'O ano {ano} É BISSEXTO.')
#else:
#    print(f'O ano {ano} NÃO É BISSEXTO.')


ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
ano_Bissexto = [x for x in range(ano, ano+10) if x % 4 == 0 and x % 100 != 0 or x % 400 == 0]
print(f'Os anos bissextos entre {ano} e {ano+10} são: {ano_Bissexto}')
if ano in ano_Bissexto:
    print(f'O ano {ano} É BISSEXTO.')
else:
    print(f'O ano {ano} NÃO É BISSEXTO.')