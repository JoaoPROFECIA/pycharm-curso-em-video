print('MAIOR E MENOR VALORES\n')
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'S':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    if resp != 'S' and 'N':
        print('Resposta inválida')
media = soma / quant
print(f'\nVocê digitou {quant} números e a média foi {media:.2f}\n'
      f'O maior número foi {maior} e o menor foi {menor}')
print('Acabou')
