print('JOGO DA ADIVINHAÇÃO v2.0\n')
from random import randint
from time import sleep
computador = randint(0, 10) # Faz o PC "pensar"
print('Sou seu computador...')
sleep(1)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(3)
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0 # Necessário para somar com 'palpites += 1'
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('O número é maior que esse... Tente mais uma vez.')
        elif jogador > computador:
            print('O número é menor que esse... Tente mais uma vez.')
if palpites < 2:
    plural1 = ''
elif palpites > 1:
    plural1 = 's'
print(f'Você acertou! O número é \033[34m{computador}\033[m e você conseguiu com \033[31m{palpites}\033[m tentativa{plural1}!')
