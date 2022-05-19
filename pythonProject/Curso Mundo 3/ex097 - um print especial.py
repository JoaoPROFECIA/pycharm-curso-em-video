def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

def linha():
    tam = '-=' * 20
    print(f'{tam}')


#  Programa principal
escreva('Teste')
escreva('Curso de Python')

linha()
