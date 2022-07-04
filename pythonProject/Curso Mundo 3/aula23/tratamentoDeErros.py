try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    c = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não digitar esse número.')
except Exception as erro:
    print(f'O erro foi {erro.__class__}')
else:
    print(f'O resultado é {c:.1f}')
finally:
    print('Volte sempre!')
