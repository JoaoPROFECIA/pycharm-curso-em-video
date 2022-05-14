print('TUPLAS COM TIMES DE FUTEBOL\n')
serieA = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthias',
          'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos',
          'Ceará SC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá',
          'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {serieA}')
print('-=' * 15)
print(f'Os 5 primeiros são: {serieA[0:5]}')
print('-=' * 15)
print(f'os 4 últimos colocados sãp {serieA[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(serieA)}')
print('-=' * 15)
print(f'O Chapecoense está em {serieA.index("Chapecoense")+1}ª posição')
