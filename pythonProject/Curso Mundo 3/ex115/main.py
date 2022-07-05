from ast import While
from lib.interface.funcoes import *
from time import sleep

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Sair'])
    if resposta == 1:
        print('Ver Pessoas Cadastradas')
    elif resposta == 2:
        print('Cadastrar Novas Pessoas')
    elif resposta == 3:
        print('Saindo do Sistema')
        for i in range(3, 0, -1):
            print('.', end='')
            sleep(0.3)
        break
    else:
        print('\033[31mOpção inválida!\033[m')
    sleep(1)
