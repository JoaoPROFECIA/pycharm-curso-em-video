print('PRIMEIRA E ULTIMA OCORRÊNCIA DE UMA STRING\n')
frase = str(input('Digite uma frase: ')).upper().strip()
print(f'\nA letra A apareceu {frase.count("A")} vezes na frase'
      f'\nA primeira letra A apareceu na posição {frase.find("A")+1}'
      f'\nA última letra A apareceu na posição {frase.rfind("A")+1}')
