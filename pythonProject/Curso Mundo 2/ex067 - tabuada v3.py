import emoji
from time import sleep

print('\033[1;90mTABUADA v3.0\033[m')
print('\033[1;94m-\033[m' * 20)
sleep(0.5)
print(emoji.emojize('\033[1;33mInsira um valor negativo para encerrar :rage:\033[m', use_aliases=True))

while True:
    print('\033[1;94m-\033[m' * 20)
    sleep(0.5)

    num = int(input('\033[1;33mQuer ver a tabuada de qual valor?\033[m '))
    print('\033[1;94m-\033[m' * 20)
    sleep(0.5)

    if num < 0: #se o número for negativo, a tabuada encerra
        print('\033[1;31mTABUADA ENCERRADA. Volte sempre!\033[m')
        break

    for c in range(1, 11): #vai fazer a tabuada de 1 até 10
        print(f'\033[1;32m{num} x {c} = {num*c}\033[m')

print(emoji.emojize(':rage:', use_aliases=True)) #um emoji qualquer
