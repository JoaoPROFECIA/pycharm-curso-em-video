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
