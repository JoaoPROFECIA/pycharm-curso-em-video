print('GERENCIADOR DE PAGAMENTOS\n')
print(f'{"LOJA DO JOÃO":=^40}\n')
preco = float(input('Preço das compras: R$'))
print('''\nFORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a forma de pagamento? '))
if opcao == 1:
    total = preco - (preco * 0.1)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de {parcela:.2f} sem juros')
elif opcao == 4:
    total = preco + (preco * 0.2)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print(f'Sua compra será parcelada em {totalparc}x de R${parcela:.2f} com juros')
else:
    total = preco
    print('OPÇÃO INVÁLIDA. Tente novamente!')
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
