a=input('Digite algo: ')
print(f'\nO tipo primitivo desse valor é {type(a)}'
      f'\nSó tem espaço? {a.isspace()}'
      f'\nÉ um número? {a.isnumeric()}'
      f'\nÉ alfabético? {a.isalpha()}'
      f'\nÉ alfanumérico? {a.isalnum()}'
      f'\nEstá em maiúsculas? {a.isupper()}'
      f'\nEstá em minúsculas? {a.islower()}'
      f'\nEstá capitalizada? {a.istitle()}')
