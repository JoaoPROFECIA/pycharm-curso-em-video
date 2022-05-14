print('JOGO DA ADIVINHAÇÃO\n')
while 1:
    from random import randint
    from time import sleep
    computador = randint(0,5) # Faz o PC "pensar"
    print('-=-' * 20)
    print('Vou pensar em um número de 0 à 5. Tente adivinhar...')
    print('-=-' * 20)
    jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
    print('PROCESSANDO...')
    sleep(1)
    if jogador == computador:
        print('PARABÉNS! Você conseguiu me vencer!')
    else:
        print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')
    input()
