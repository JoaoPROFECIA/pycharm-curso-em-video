from dados import leiaInt, leiaFloat
"""
Função que faz a leitura de um número inteiro e flutuante.
"""
num = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número {num}')
print(f'Você acabou de digitar o número {real}'.replace('.', ','))