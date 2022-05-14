print('CUSTO DA VIAGEM\n')
dist = float(input('Qual é a distancia da sua viagem? '))
if dist <= 200:
    custo = dist * 0.5
    print(f'Você está prestes a começar uma viagem de {dist}km.'
          f'\nE o preço da sua viagem será de {custo}')
else:
    custo = dist * 0.45
    print(f'Você está prestes a começar uma viagem de {dist}km.'
          f'\nE o preço da sua viagem será de {custo}')
