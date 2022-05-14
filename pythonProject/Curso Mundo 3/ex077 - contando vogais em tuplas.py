print('CONTANDO VOGAIS EM TUPLAS')
print('-=' * 25)
palavra = []
continuar = ' '
while True:
    palavra.append(str(input('Digite uma palavra: ')).strip())
    continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Resposta inválida. Quer continuar? [S/N] ')).strip().lower()[0]
    if continuar == 's':
        continue
    if continuar == 'n':
        break
print('-=' * 25)
for p in palavra:
    print(f'\nNa palavra {p.upper()} temos as vogais ', end='')
    for letra in p:
        if letra.lower() in 'aáàãâeéèêiíìîoõôóòuûúù':
            print(letra.lower(), end=' ')
print()
print('-=' * 25)

#('aprender', 'programar', 'linguagem', 'python', 'curso',
#           'grátis', 'estudar', 'praticar', 'trabalhar')
