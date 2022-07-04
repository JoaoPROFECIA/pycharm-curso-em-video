def aumentar(preço=0, taxa=0, formato=False):
    '''
    Recebe um preço e aumenta com a porcentagem informada
    :param preço:
    :param taxa:
    :param formato:
    :return:
    '''
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    '''
    Recebe um preço e diminui com a porcentagem informada
    :param preço:
    :param taxa:
    :param formato:
    :return:
    '''
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    '''
    Recebe um preço e retorna o dobro dele
    :param preço:
    :param formato:
    :return:
    '''
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    '''
    Recebe um preço e retorna a metade dele
    :param preço:
    :param formato:
    :return:
    '''
    res = preço / 2
    return res if formato is False else moeda(res)
 

def moeda(preço=0, moeda = 'R$'):
    '''
    Recebe um preço e retorna o valor formatado
    :param preço:
    :param moeda:
    :return:
    '''
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxa=10, taxa2=5):
    '''
    Recebe um preço e mostra um resumo do valor com as taxas informadas
    :param preço:
    :param taxa:
    :param taxa2:
    :return:
    '''
    print('-' * 34)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 34)
    print(f'Preço analisado:\t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço:\t{metade(preço, True)}')
    print(f'{taxa}% de aumento: \t{aumentar(preço, taxa, True)}')
    print(f'{taxa2}% de redução: \t{diminuir(preço, taxa2, True)}')
    print('-' * 34)
