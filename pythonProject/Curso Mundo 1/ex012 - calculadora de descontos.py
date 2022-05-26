#while 1:
#    print('CALCULADORA DE DESCONTOS\n')
#    preço = float(input('Insira o valor do produto: R$'))
#    porcentagem = float(input('Quantos % de desconto você quer? '))
#    desc = preço-(preço*porcentagem/100)
#    print(f'O produto que custava R${preço:.2f}, na promoção vai custar R${desc:.2f}.')
#    input()
#    print('--'*20)
#    print('\n')

def desconto(preço, porcentagem):
    desc = preço-(preço*porcentagem/100)
    return desc

def linha():
    print('-='*30)


preço = float(input('Insira o valor do produto: R$'))
porcentagem = float(input('Quantos % de desconto você quer? '))
print(f'O produto que custava R${preço:.2f}, na promoção vai custar R${desconto(preço, porcentagem):.2f}.')
linha()