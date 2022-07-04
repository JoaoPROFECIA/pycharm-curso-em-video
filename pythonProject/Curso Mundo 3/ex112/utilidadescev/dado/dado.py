def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31m ERRO! "{entrada}" é valor inválido\033[m')
        else:
            válido = True
            return float(entrada)


