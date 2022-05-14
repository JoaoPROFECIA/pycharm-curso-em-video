print('VERDADE OU DESAFIO\n')
from random import shuffle

v1 = 'Já fez algo de que se arrependa? Se sim o que?'
v2 = 'Ja tirou o BV?'
v3 = 'Você tem um dia inesquecível? Se sim como foi?'
v4 = 'Você ja desistiu de algo muito importante? Se sim o que foi?'
v5 = 'Já sofreu ou praticou bullying na escola?'
v6 = 'Tem algum grande desejo? Qual?'
v7 = 'Ja entrou em uma briga? Como foi?'
v8 = 'Você quer ter filhos? Se sim quantos?'

d1 = 'Imite um macaco'
d2 = 'Deixe a pessoa do seu lado direito te dar um tapa'
d3 = 'Teve sorte, pule a sua vez'
d4 = 'Fale uma raça de cachorro que começa com y, se não conseguir imite um '
d5 = 'Não fale nada pelos próximos 5 minutos'
d6 = 'Fale para uma pessoa que não está na brincadeira que a ama (não vale parente)'
d7 = 'Você so poderá escolher desafio nas próximas 5 rodadas'
d8 = 'Agora você tem poder, mande um dos jogadores fazer o que você quiser'

lista_v = [v1, v2, v3, v4, v5, v6, v7, v8]
lista_d = [d1, d2, d3, d4, d5, d6, d7, d8]

print('Caso queira verdade escreva V, se quiser desafio escreva D.')

while True:
  shuffle(lista_v)
  shuffle(lista_d)

  d_v = input('Você escolhe verdade ou desafio? ')

  if d_v == 'v' :
    print(f'{lista_v[0]}\n')
  elif d_v == 'd':
    print(f'{lista_d[0]}\n')