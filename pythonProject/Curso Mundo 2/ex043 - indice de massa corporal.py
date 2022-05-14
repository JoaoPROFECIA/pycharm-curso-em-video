print('ÍNDICE DE MASSA CORPORAL\n')
peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / pow(altura, 2)
print(f'O IMC dessa pessoa é de {imc:.1f}.')
if imc < 18.5:
    print('Você está abaixo do peso normal.')
elif imc < 25:
    print('Você está no peso ideal.')
elif imc < 30:
    print('Você está em sobrepeso.')
elif imc < 40:
    print('Você está em obesidade.')
elif imc > 40:
    print('Você está em obesidade mórbida.')
