def linha30():
    msg = '-=' * 30
    print(msg)
    
def maior(* num):
    cont = maior = 0
    linha30()
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


#programa principal
maior(1,2,3)
maior(4, 7, 0)
maior(6,3,5,8,4,2,3)
linha30()