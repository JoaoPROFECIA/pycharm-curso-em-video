print('ANALISADOR DE TEXTOS\n')
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Analisando seu nome...'
      f'\nSeu nome em maiúsculas é {nome.upper()}'
      f'\nSeu nome em minúsculas é {nome.lower()}'
      f'\nSeu nome tem ao todo {len(nome) - nome.count(" ")} letras')
#print(f'Seu primeiro nome tem {nome.find(" ")} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])}')
