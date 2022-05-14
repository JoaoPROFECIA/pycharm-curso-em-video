print('ANALISADOR COMPLETO\n')
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for pessoa in range(1, 5):
    print(f'----- {pessoa}ª PESSOA -----')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if pessoa == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 +=1
mediaidade = somaidade / 4
print(f'\nA média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
if totmulher20 > 1:
    plural1 = 'são'
    plural2 = 'es'
else:
    plural1 = 'é'
    plural2 = ''
print(f'Ao todo {plural1} {totmulher20} mulher{plural2} com menos de 20 anos')
