print('NÚMERO POR EXTENSO\n')
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
        'nove', 'dez', 'onze', 'dose', 'treze', 'quatorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
                print(f'Você digitou o número {cont[num]}')
                continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()
                if continuar in 'S':
                        continue
                if continuar in 'N':
                        print('O programa foi encerrado')
                        break
        print('Tente novamente. ', end='')
