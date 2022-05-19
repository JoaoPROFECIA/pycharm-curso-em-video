from time import sleep
def linha20():
    tam = '-=' * 20
    print(f'{tam}')

def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1 
    linha20()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
       
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.2)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.2)
            cont -= p
        print('FIM!')
    
    
# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
linha20()
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)