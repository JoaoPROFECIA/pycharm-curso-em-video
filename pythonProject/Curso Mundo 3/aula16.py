print('-='*35)
num = [2, 5, 9, 1]

b = num[:] #os dois pontos fazem uma cópia fiel da primeira lista

b[2] = 5
print(f'Lista A: {num}')
print(f'Lista B: {b}')
print('-='*35)

num[2] = 3 #troca o valor do segundo elemento, começando a contagem em zero
num.append(7) #adiciona um número à lista
num.sort() #deixa em ordem crescente
num.sort(reverse=True) #deixa em ordem decrescente
num.insert(2, 0) #vai colocar o 0 na posição 2, passando os demais pra frente
#num.pop(2) #se vazio, exclui o último elemento.

if 4 in num:
    num.remove(4) #remove o primeiro numero do valor informado da lista
else:
    print('Não achei o número 4')

print(num)
print(f'Essa lista tem {len(num)} elementos')
print('-='*35)
valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print('-' * 70)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...')

print('Cheguei ao final da lista')
print('-='*35)
