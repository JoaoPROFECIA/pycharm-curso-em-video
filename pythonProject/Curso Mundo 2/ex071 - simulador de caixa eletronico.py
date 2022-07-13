from time import sleep
class Conta:
    def titulo():
        print('SIMULADOR DE CAIXA ELETRÔNICO\n')


    def linha():
        print('-' * 30)


    def menu():
        print('1 - Saque')
        print('2 - Depósito')
        print('3 - Saldo')
        print('4 - Sair')
        print('\n')
        while True:
            opcao = int(input('Digite a opção desejada: '))
            if opcao == 1:
                Conta.saque()
            elif opcao == 2:
                Conta.deposito()
            elif opcao == 3:
                Conta.saldo()
            elif opcao == 4:
                print('Saindo do sistema', end='')
                for i in range(3):
                    print('.', end='')
                    sleep(0.3)
                break
            else:
                print('Opção inválida!')
                Conta.linha()
                Conta.menu()


    def saque():
        Conta.linha()
        Conta.menu()
        valor = int(input('Que valor você quer sacar? R$'))
        total = valor
        ced = 50
        totced = 0
        while True:
            if total >= ced:
                total -= ced
                totced += 1
            else:
                if totced > 0:
                    print(f'Total de {totced} cédulas de R${ced}')
                if ced == 50:
                    ced = 20
                elif ced == 20:
                    ced = 10
                elif ced == 10:
                    ced = 1
                totced = 0
                if total == 0:
                    break


Conta.linha()
Conta.titulo()
Conta.menu()

print('Volte sempre ao BANCO DO JOÃO! Tenha um bom dia!')
