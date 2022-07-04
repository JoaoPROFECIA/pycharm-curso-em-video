try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    c = a / b
except Exception as erro:
    print(f'Infelizmente ocorreu um erro!\nO erro foi: {erro.__class__}')
else:
    print(f'O resultado é {c:.1f}')
finally:
    print('Volte sempre!')