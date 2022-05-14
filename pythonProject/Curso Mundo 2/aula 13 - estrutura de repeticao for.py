print('ESTRUTURA DE REPETIÇÃO - FOR\n')
while 1:
    print('''Escolha qual exercício quer executar
    [ 1 ] para Exercício 1
    [ 2 ] para Exercício 2 
    [ 3 ] para exercício 3 
    [ 4 ] para Exercício 4
    [ 5 ] para Exercício 5
    [ 6 ] para Exercício 6\n''')
    escolha = int(input('Digite um nº de 1 à 6 para continuar: '))
    if escolha == 1:
        for c in range(0, 6):
            print('Oi')
    if escolha == 2:
        for c in range(0, 6):
            print(c)
    if escolha == 3:
        for c in range(6, 0, -1):
            print(c)
    if escolha == 4:
        i = int(input('Início: '))
        f = int(input('Fim: '))
        p = int(input('Passo: '))
        for c in range(i,f+1, p):
            print(c)
    if escolha == 5:
        for c in range(0,3):
            n = int(input('Digite um valor: '))
    if escolha == 6:
        s = 0
        for c in range(0, 4):
            n = int(input('Digite um valor: '))
            s += n
        print(f'O somatório de todos os valores foi {s}\n')
    print('FIM\n')
    input('Pressione Enter para continuar.')
