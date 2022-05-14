print('RADAR ELETRÔNICO 80km/h\n')
while 1:
    velocidade = float(input('Qual é a velocidade atual do carro? '))
    if velocidade > 80:
        print('\nMULTADO! Você excedeu o limite de segurança!')
        multa = (velocidade-80) * 7
        print(f'Você deve pagar uma multa de R${multa:.2f}!')
    print('\nTenha um bom dia! Dirija com segurança!')
    print('-=-' * 20)
    input()