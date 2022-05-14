print('SEQUENCIA DE FIBONACCI\n')
n = int(input('\033[1;35mQuantos termos você quer mostrar?\033[m '))
t1 = 0
t2 = 1
print('~'*30)
print(f'\033[1;94m{t1} → {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' - FIM\033[m')
