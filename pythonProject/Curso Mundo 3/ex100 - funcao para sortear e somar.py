from random import randint
from time import sleep


def linha30():
    msg = '-=' * 30
    print(msg)


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.2)
    print('PRONTO!')
    sleep(0.5)


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor %2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
    sleep(0.5)


def somaImpar(lista):
    soma = 0
    for valor in lista:
        if valor %2 == 1:
            soma += valor
    print(f'Somando os valores ímpares de {lista}, temos {soma}')
    sleep(0.5)


def somaLista(lista):
    soma = 0
    for valor in lista:
        soma += valor
    print(f'Somando todos os valores da lista, temos {soma}')
    sleep(0.5)


def maior(lista):
    maior = lista[0]
    for valor in lista:
        if valor > maior:
            maior = valor
    print(f'O maior valor da lista é {maior}')
    sleep(0.5)


def menor(lista):
    menor = lista[0]
    for valor in lista:
        if valor < menor:
            menor = valor
    print(f'O menor valor da lista é {menor}')
    sleep(0.5)


numeros = list()
sorteia(numeros)
linha30()
somaPar(numeros)
linha30()
somaImpar(numeros)
linha30()
maior(numeros)
linha30()
menor(numeros)
linha30()
somaLista(numeros)
linha30()
