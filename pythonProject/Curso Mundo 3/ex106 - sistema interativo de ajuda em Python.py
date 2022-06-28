# Sistema interativo de ajuda em Python

from time import sleep

c = ('\033[m',     #0 - sem cor
     '\033[1;30m', #1 - preto
     '\033[1;31m', #2 - vermelho
     '\033[1;32m', #3 - verde
     '\033[1;33m', #4 - amarelo
     '\033[1;34m', #5 - azul
     '\033[1;35m', #6 - roxo
     '\033[1;36m', #7 - azul claro
     '\033[1;37m', #8 - branco 
     '\033[1;38m', #9 - cinza
     '\033[1;39m', #10 - branco
     '\033[1;40m', #11 - cinza
     '\033[1;41m', #12 - vermelho claro
     '\033[1;42m', #13 - verde claro
     '\033[1;43m', #14 - amarelo claro
     '\033[1;44m', #15 - azul claro
     '\033[1;45m', #16 - roxo claro
     '\033[1;46m', #17 - azul claro
     '\033[1;47m', #18 - branco
     '\033[1;48m', #19 - cinza
     '\033[1;49m', #20 - branco
     '\033[1;50m', #21 - cinza
     '\033[1;51m'  #22 - vermelho claro
    )


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 2)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msm, cor=0):
    tam = len(msm) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msm}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa principal
comando=''
while True:
    título('SISTEMA DE AJUDA PyTHON', 2)
    comando = str(input('Função ou Biblioteca: ')).strip().lower()
    if comando.upper().strip() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ MAIS!', 5)