print('VALIDAÇÃO DE DADOS\n')
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
if sexo == 'M':
    genero = 'masculino'
if sexo == 'F':
    genero = 'feminino'
print(f'Sexo {genero} registrado com sucesso.\n')
idade = int(input('Informe sua idade: '))
while idade not in range(0, 131):
    idade = int(input('Dados inválidos. Por favor, informe sua idade: '))
print('Idade registrada com sucesso.')
