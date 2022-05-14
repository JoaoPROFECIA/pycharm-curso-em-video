from time import sleep
print('CRIANDO MENU DE OPÇÕES\n')
print('Bem vindo!')
opcao = 0
while opcao != 5: #enquanto a opção for diferente de 5, o programa continuará a ser executado
      print('''\n[1] Somar
[2] Multiplicar
[3] Maior número
[4] Novos números
[5] Sair do programa''')
      opcao = int(input('\nEscolha um número: '))
      if opcao in range(1, 5): #se opção for um número entre 1 e 5, os comando abaixo serão executados
            num1 = int(input('\nPrimeiro número: '))
            num2 = int(input('Segundo número: '))
            if opcao == 1: #soma
                  tot = num1 + num2
                  print(f'O resultado da soma é \033[34m{tot}\033[m')
            elif opcao == 2: #multiplicação
                  tot = num1 * num2
                  print(f'O resultado da multiplicação é \033[34m{tot}\033[m')
            elif opcao == 3: #maior número entre os dois
                  if num1 > num2: #maior que...
                        maior = num1
                        print(f'Entre os dois números, o maior é \033[34m{maior}\033[m')
                  if num1 < num2: #menor que...
                        maior = num2
                        print(f'Entre os dois números, o maior é \033[34m{maior}\033[m')
                  if num1 == num2: #se os números  forem iguais...
                        print('Os dois números são iguais!')
            elif opcao == 4: #para calcular novos números
                  input('Novos números. Pressione ENTER para continuar.\n')
            continuar = str(input('\nDeseja continuar? [S/N] ')).strip().upper()[0] #.strip tira os espaços do inicio e .upper deixa em maiúsculo. [0] pega somente a primeira letra da palavra > 'S' ou 'N'
            if continuar == 'S':
                  input('Novos números. Pressione ENTER para continuar.\n')
            if continuar == 'N':
                  print('Finalizando...')
                  sleep(2)
                  break #comando para encerrar
      if opcao == 5:
            print('Finalizando...')
            sleep(2)
            break  #comando para encerrar
      if opcao not in range(1,5): #se o número for algo fora do range de 1 a 5, apresente: 'Opção inválida'
            print('Opção inválida. Tente novamente.')
