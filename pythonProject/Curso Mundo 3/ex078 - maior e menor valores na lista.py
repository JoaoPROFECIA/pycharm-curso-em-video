from time import sleep
print('MAIOR E MENOR VALORES NA LISTA')
sleep(0.5)
print('-='*30)
valores = []
maior = menor = 0
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
    sleep(0.2)
print('-='*30)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
    sleep(0.3)
print('-='*30)
print(f'O maior valor foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'e o menor {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()
print('-='*30)
