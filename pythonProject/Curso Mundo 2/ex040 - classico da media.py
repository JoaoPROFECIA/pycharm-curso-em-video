print('AQUELE CLÁSSICO DA MÉDIA\n')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a média do aluno é {media:.2f}.')
if media >= 7:
    print('Parabéns, você foi aprovado!')
elif media < 6:
    print('Você está reprovado!')
elif media > 6 and media < 7:
    print('Você está de recuperação!')
