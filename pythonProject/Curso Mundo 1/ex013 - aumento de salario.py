while 1:
    from time import sleep
    print('AUMENTO DE SALÁRIO')
    sleep(1)
    salário = float(input('\nQual é o salário do funcionário: R$'))
    porcentagem = float(input('Aumento salarial em porcentagem: %'))
    aumento_salarial = salário + (salário * porcentagem / 100)
    print(f'\nO funcionário que ganhava {salário:.2f} passa a receber R${aumento_salarial:.2f}')
    print(input('Pressione enter para continuar.'))
    print('---'*20)
    print('\n')
    sleep(1)
