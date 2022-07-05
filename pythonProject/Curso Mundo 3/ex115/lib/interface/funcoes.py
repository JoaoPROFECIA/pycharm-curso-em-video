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


def linha(tam = 42):
    """
    Função que retorna uma string com o caractere '-' de acordo com o tamanho passado por parâmetro.
    :param tam: Tamanho da string.
    :return: Retorna uma string com o caractere '-' de acordo com o tamanho passado por parâmetro.
    """
    return '-' * tam


def cabecalho(txt):
    """
    Função que exibe o cabeçalho do programa.
    :param txt: Texto a ser exibido no cabeçalho.
    """
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    """
    Função que exibe o menu do programa.
    :param lista: Lista com as opções do menu.
    :return: Retorna a opção selecionada pelo usuário.
    """
    cabecalho('MENU PRINCIPAL')
    for i, item in enumerate(lista):
        print(f'\033[33m{i+1}\033[m) \033[34m{item}\033[m')
    print(linha())
    opcao = leiaInt('\033[32mSua opção: \033[m')
    return opcao


