def leiaInt(msg):
    """
    Função que faz a leitura de um número inteiro.
    :param msg: Mensagem a ser exibida para o usuário.
    :return: Retorna o número inteiro digitado.
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31m[Erro] Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31m[Erro] O usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    """
    Função que faz a leitura de um número real.
    :param msg: Mensagem a ser exibida para o usuário.
    :return: Retorna o número real digitado.
    """
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[31m[Erro] Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31m[Erro] O usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
