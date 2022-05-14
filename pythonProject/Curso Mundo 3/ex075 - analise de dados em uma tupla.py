print('ANÁLISE DE DADOS EM UMA TUPLA\n')
valor = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o último número: ')))
print(f'Você digitou os valores {valor}')
print(f'O 9 apareceu {valor.count(9)} vezes')

if 3 in valor:
    print(f'O valor 3 apareceu na {valor.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')

for n in valor:
    if n % 2 == 0:
        print(n, end=' ')
