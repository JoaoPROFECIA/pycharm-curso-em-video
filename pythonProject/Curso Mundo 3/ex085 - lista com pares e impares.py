print('LISTA COM PARES E ÍMPARES')
print('-=' * 30)

num = [[], []] #lista dentro de outra lista > de valor: '[['0'], ['1']]'
valor = 0 #teste lógico

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor) #append() é pra ir adicionando números à lista "valor"
    else:
        num[1].append(valor)

num[0].sort() #sort() vai enumerar em ordem crescente
num[1].sort()

print('-=' * 30)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
