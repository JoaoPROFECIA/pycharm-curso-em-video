print('ANÁLISE DE DADOS DO GRUPO\n')
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Quantos anos você tem? '))
    sexo = plural1 = plural2 = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
        if totH == 0:
            plural1 = 'Nenhum homem foi cadastrado'
        if totH == 1:
            plural1 = 'homem foi cadastrado'
        if totH > 1:
            plural1 = 'homens foram cadastrados'
    if sexo == 'F' and idade < 20:
        totM20 += 1
        if totM20 == 0:
            plural2 = 'nenhuma mulher tem'
        if totM20 == 1:
            plural2 = 'mulher tem'
        if totM20 > 1:
            plural2 = 'mulheres têm'
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Com base nos dados coletados:\n'
      f'{tot18} pessoas tem mais de 18 anos.\n'
      f'{totH} {plural1}\n'
      f'e {totM20} {plural2} menos de 20 anos')