print('APROVANDO EMPRÉSTIMO')
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
ano = int(input('Quantos anos de financiamento? '))
prestacao = casa / (ano * 12)
minimo = salario * 0.3
print(f'Para pagar uma casa de R${casa:.2f} em {ano} anos, a prestação será de {prestacao:.2f}.')
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')