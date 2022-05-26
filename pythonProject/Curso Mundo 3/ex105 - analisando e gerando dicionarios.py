def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)

    cores = dict()
    cores['verde'] = '\033[1;32m'
    cores['amarelo'] = '\033[1;33m'
    cores['vermelho'] = '\033[1;31m'
    cores['limpa'] = '\033[m'

    if sit:
        if r['média'] >= 7:
            r['situação'] = print('\033[1;32mBOA\033[m')
        elif r['média'] >= 5:
            r['situação'] = print('\033[1;33mRAZOAVEL\033[m')
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5.5, 2, 10, sit=True)
print(resp)
