from time import sleep
from random import randint

lista = list()
jogos = list()

print('-' * 30)
print(f'{"PALPITES PARA A MEGA DA VIRADA":^30}')
print('-' * 30)
print()
quant = int(input('Quantos jogos você quer que eu sorteie? '))

tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print()
sleep(0.2)
print('-=' * 4, f'SORTEANDO {quant} JOGOS', '-=' * 4)
print()

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)

print()
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
