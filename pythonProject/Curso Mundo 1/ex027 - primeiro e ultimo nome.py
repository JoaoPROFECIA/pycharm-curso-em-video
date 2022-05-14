print('PRIMEIRO E ULTIMO NOME DE UMA PESSOA\n')
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(f'Seu primeiro nome é {nome[0]} e seu último nome é {nome[len(nome)-1]}')
