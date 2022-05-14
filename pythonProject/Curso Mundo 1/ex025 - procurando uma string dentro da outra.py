print('PROCURANDO UMA STRING DENTRO DA OUTRA\n')
nome = str(input('Digite seu nome: ')).lower().strip().split()
print(f'Seu nome tem Silva? {"silva" in nome}')
