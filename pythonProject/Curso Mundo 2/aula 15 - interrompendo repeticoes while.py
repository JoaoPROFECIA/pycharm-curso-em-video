print('INTERROMPENDO REPETIÇÕES WHILE\n')
cont = n = s = 0
while True:
    n = int(input('Insira o valor desejado [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    s += n
    if cont == 1:
        plural1 = 'foi'
    if cont > 1:
        plural1 = 'foram'
print(f'O total de números informados {plural1} {cont} e o total da soma é {s}')
