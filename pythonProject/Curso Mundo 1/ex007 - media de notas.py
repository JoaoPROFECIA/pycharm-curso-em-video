print('MÉDIA DE NOTAS\n')


def media_Notas():
    n1 = float(input('Primeira nota do aluno: '))
    n2 = float(input('Segunda nota do aluno: '))
    m = (n1+n2)/2
    print(f'\nA média entre {n1} e {n2} é {m:.2f}')
    if m >= 6.0:
        print('Média boa! PARABÉNS!')
    else:
        print('Média ruim! ESTUDE MAIS!')


media_Notas()
