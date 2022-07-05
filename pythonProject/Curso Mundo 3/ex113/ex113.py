def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31m[Erro] Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31m[Erro] O usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


num = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {num}')
