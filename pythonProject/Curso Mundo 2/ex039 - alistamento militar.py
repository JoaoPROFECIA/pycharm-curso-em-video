print('ALISTAMENTO MILITAR\n')
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem ou terá {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!\n')
    input('Pressione Enter para recalcular.\n\n')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Ainda faltam {saldo} anos para o alistamento\n'
          f'Seu alistamento será em {ano}\n')
    input('Pressione Enter para recalcular.\n\n')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você já deveria ter se alistado há {saldo} anos\n'
          f'Seu alistamento foi em {ano}\n')
    input('Pressione Enter para recalcular.\n\n')
