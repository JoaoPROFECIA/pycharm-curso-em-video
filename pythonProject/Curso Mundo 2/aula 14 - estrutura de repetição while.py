print('ESTRUTURA DE REPETIÇÃO WHILE\n')
'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
    if par == 1:
        plural1 = 'numero par'
    if par > 1:
        plural1 = 'números pares'
    if impar == 1:
        plural2 = 'número ímpar'
    if impar > 1:
        plural2 = 'números ímpares'
print(f'Você digitou {par} {plural1} e {impar} {plural2}!')
