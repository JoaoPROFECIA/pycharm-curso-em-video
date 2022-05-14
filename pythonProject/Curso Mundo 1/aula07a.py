def main() -> object:
    n1 = int(input('Digite um valor: \n'))
    n2 = int(input('Digite Outro valor: \n'))
    s = n1 + n2
    m = n1 * n2
    d = n1 / n2
    di = n1 // n2
    e = n1 ** n2
    print(f'A soma é {s} '
          f'\nA multiplicação é {m} '
          f'\nA divisão é {d}', end=
          f'\nA divisão inteira é {di} '
          f'\nE a potência é {e}.\n\n')

#-----
main()
def main() -> object:
    n = int(input("Digite o valor de n: "))
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1

    print("O valor de %d! eh =" %n, fat)

#-----
main()
